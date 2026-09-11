"""HTTP-транспорт к серверу ККМ."""

from __future__ import annotations

import base64
import ipaddress
import threading
import urllib.request
from datetime import timedelta
from typing import Any, Optional
from urllib.parse import quote, urlunsplit

import httpx

from rbsoftskkm.data import json_codec
from rbsoftskkm.data.response_result import ResponseResult

API_PATH = "/PrintService/api/v4"
JSON_MEDIA_TYPE = "application/json; charset=utf-8"
DEFAULT_TIMEOUT = timedelta(seconds=60)


class CancelToken:
    """Отмена текущего запроса из другого потока.

    Ожидание ответа и отмена живут в разных потоках: запрос выполняется в
    рабочем потоке, вызывающий ждёт одно событие — ответ или отмену.
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._cancelled = False
        self._finished: Optional[threading.Event] = None
        self._response: Optional[httpx.Response] = None

    @property
    def cancelled(self) -> bool:
        with self._lock:
            return self._cancelled

    def cancel(self) -> None:
        with self._lock:
            self._cancelled = True
            response = self._response
            finished = self._finished
        if response is not None:
            try:
                response.close()
            except Exception:
                pass
        if finished is not None:
            finished.set()

    def _attach_event(self, finished: threading.Event) -> None:
        with self._lock:
            self._finished = finished
            cancelled = self._cancelled
        if cancelled:
            finished.set()

    def _attach_response(self, response: httpx.Response) -> None:
        with self._lock:
            self._response = response
            cancelled = self._cancelled
        if cancelled:
            try:
                response.close()
            except Exception:
                pass


class KkmTransport:
    """Клиент REST API сервера ККМ: адрес, заголовки, разбор конверта ответа."""

    def __init__(self) -> None:
        # Клиент создаётся при первом запросе: httpx загружает корневые сертификаты
        # при создании, а для HTTP они не нужны — иначе секунды на пустом месте.
        self._client: Optional[httpx.Client] = None
        self._client_key = (False, False)
        self._proxy_by_host: dict[str, bool] = {}
        self._disposed = False

        self.Host: str = "localhost"
        self.Port: int = 4398
        self.UseHttps: bool = False
        self.Token: Optional[str] = None
        self.TerminalId: Optional[str] = None
        self.BasicAuthUser: Optional[str] = None
        self.BasicAuthPassword: Optional[str] = None
        self.Timeout: timedelta = DEFAULT_TIMEOUT

    # ------------------------------------------------------------- запросы

    def Get(self, path: str, use_basic_auth: bool = False, cancel: Optional[CancelToken] = None) -> ResponseResult:
        return self._send("GET", path, None, use_basic_auth, cancel)

    def Post(self, path: str, body: Any = None, cancel: Optional[CancelToken] = None) -> ResponseResult:
        return self._send("POST", path, body, False, cancel)

    def Put(self, path: str, body: Any = None, cancel: Optional[CancelToken] = None) -> ResponseResult:
        return self._send("PUT", path, body, False, cancel)

    def Delete(self, path: str, cancel: Optional[CancelToken] = None) -> ResponseResult:
        return self._send("DELETE", path, None, False, cancel)

    def Dispose(self) -> None:
        if self._disposed:
            return
        self._disposed = True
        if self._client is not None:
            self._client.close()

    def _ensure_client(self) -> httpx.Client:
        # Проверка исключений прокси может обращаться к DNS — считаем её один раз на хост.
        use_proxy = self._proxy_by_host.get(self.Host)
        if use_proxy is None:
            use_proxy = self._proxy_by_host[self.Host] = uses_system_proxy(self.Host)

        key = (self.UseHttps, use_proxy)
        if self._client is not None and self._client_key == key:
            return self._client

        if self._client is not None:
            self._client.close()

        self._client = httpx.Client(
            timeout=None,
            limits=httpx.Limits(keepalive_expiry=60.0),
            follow_redirects=True,
            verify=self.UseHttps,
            trust_env=use_proxy,
        )
        self._client_key = key
        return self._client

    # ------------------------------------------------------------ механика

    def _send(
        self,
        method: str,
        relative_url: str,
        body: Any,
        use_basic_auth: bool,
        cancel: Optional[CancelToken],
    ) -> ResponseResult:
        if self._disposed:
            return fail_result(-1, "Коннектор закрыт. Создайте новый SkkmConnector.")
        if not self.Host.strip() or not 1 <= self.Port <= 65535:
            return fail_result(-1, "Укажите Host и Port сервера ККМ.")

        timeout = self.Timeout if self.Timeout > timedelta(0) else DEFAULT_TIMEOUT
        request = self._build_request(method, relative_url, body, use_basic_auth, timeout.total_seconds())
        outcome: dict[str, Any] = {}
        finished = threading.Event()

        def worker() -> None:
            try:
                outcome["value"] = self._execute(request, cancel)
            except BaseException as error:  # noqa: BLE001 - ошибка уходит в результат вызова
                outcome["error"] = error
            finally:
                finished.set()

        if cancel is not None:
            cancel._attach_event(finished)

        thread = threading.Thread(target=worker, name="skkm-request", daemon=True)
        thread.start()
        finished.wait()

        if "value" in outcome:
            return outcome["value"]
        if cancel is not None and cancel.cancelled:
            return fail_result(-3, "Запрос отменён")
        error = outcome.get("error")
        if isinstance(error, httpx.TimeoutException):
            return fail_result(-2, "Превышено время ожидания ответа сервера")
        if isinstance(error, httpx.RequestError):
            return fail_result(-1, f"Ошибка соединения: {error}")
        if error is not None:
            return fail_result(-1, f"Ошибка соединения: {error}")
        return fail_result(-3, "Запрос отменён")

    def _execute(self, request: httpx.Request, cancel: Optional[CancelToken]) -> ResponseResult:
        try:
            response = self._ensure_client().send(request, stream=True)
        except httpx.TimeoutException:
            return fail_result(-2, "Превышено время ожидания ответа сервера")
        except httpx.RequestError as error:
            if cancel is not None and cancel.cancelled:
                return fail_result(-3, "Запрос отменён")
            return fail_result(-1, f"Ошибка соединения: {error}")

        if cancel is not None:
            cancel._attach_response(response)

        try:
            response.read()
            body_text = response.text
        except httpx.TimeoutException:
            return fail_result(-2, "Превышено время ожидания ответа сервера")
        except httpx.RequestError as error:
            if cancel is not None and cancel.cancelled:
                return fail_result(-3, "Запрос отменён")
            return fail_result(-1, f"Ошибка соединения: {error}")
        finally:
            response.close()

        status_code = response.status_code
        if not body_text.strip():
            return fail_result(status_code, describe_http_error(status_code, reason_phrase(status_code)))

        try:
            parsed = json_codec.loads(body_text)
        except ValueError:
            return fail_result(status_code, describe_http_error(status_code, "некорректный ответ сервера"))

        if isinstance(parsed, dict):
            result = json_codec.from_json(ResponseResult, parsed)
            if isinstance(result, ResponseResult):
                return result
        return fail_result(status_code, describe_http_error(status_code, "некорректный ответ сервера"))

    def _build_request(
        self,
        method: str,
        relative_url: str,
        body: Any,
        use_basic_auth: bool,
        timeout_seconds: float,
    ) -> httpx.Request:
        headers: dict[str, str] = {}
        if use_basic_auth:
            user = self.BasicAuthUser or ""
            password = self.BasicAuthPassword or ""
            token = base64.b64encode(f"{user}:{password}".encode()).decode("ascii")
            headers["Authorization"] = f"Basic {token}"
        else:
            if self.Token:
                headers["api_key"] = self.Token
            if self.TerminalId:
                headers["TerminalId"] = self.TerminalId

        content: Optional[bytes] = None
        if body is not None and method not in ("GET", "DELETE"):
            content = json_codec.dumps(body).encode("utf-8")
            headers["Content-Type"] = JSON_MEDIA_TYPE

        return self._ensure_client().build_request(
            method,
            self._request_url(relative_url),
            headers=headers,
            content=content,
            timeout=timeout_seconds,
        )

    def _request_url(self, relative_url: str) -> str:
        path, _, query = relative_url.partition("?")
        scheme = "https" if self.UseHttps else "http"
        full_path = f"{API_PATH}/{path.lstrip('/')}"
        return urlunsplit((scheme, f"{self.Host}:{self.Port}", full_path, query, ""))


def escape_data(value: str) -> str:
    """Значение query-параметра, как Uri.EscapeDataString."""
    return quote(value, safe="")


def uses_system_proxy(host: str) -> bool:
    """Нужен ли системный прокси для адреса сервера ККМ."""
    # httpx берёт прокси из настроек Windows, но не читает их список исключений.
    name = host.strip().strip("[]")
    if name.lower() == "localhost":
        return False
    try:
        if ipaddress.ip_address(name).is_loopback:
            return False
    except ValueError:
        pass
    return not urllib.request.proxy_bypass(name)


def fail_result(code: int, description: str) -> ResponseResult:
    return ResponseResult(Code=code, Description=description, Success=False, Result=None)


def describe_http_error(status_code: int, fallback: str) -> str:
    if status_code == 401:
        return "Ошибка авторизации. Укажите токен или включите анонимный доступ на сервере ККМ."
    if status_code == 403:
        return "Доступ запрещён. Проверьте токен API."
    return f"Ошибка HTTP {status_code}: {fallback}"


def reason_phrase(status_code: int) -> str:
    phrase = httpx.codes.get_reason_phrase(status_code)
    return phrase or str(status_code)
