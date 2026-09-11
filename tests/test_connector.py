"""Проверки коннектора без живого сервера: транспорт, сериализация, разбор ответа.

Запуск: python -m unittest discover -s tests
"""

from __future__ import annotations

import json
import threading
import time
import unittest
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any, Optional
from unittest import mock

import httpx

SOURCE_ROOT = Path(__file__).resolve().parent.parent / "src"
if str(SOURCE_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(SOURCE_ROOT))

from rbsoftskkm import (  # noqa: E402
    Cashier,
    CheckType,
    FiscalLine,
    Payments,
    SkkmConnector,
    TaxSystem,
)
from rbsoftskkm.data.kkm_transport import KkmTransport, uses_system_proxy  # noqa: E402

FISCAL_RESULT = {
    "docId": "0AC0B2E1",
    "fiscalSign": "1234567890",
    "shiftNumber": 7,
    "fiscalNumber": 42,
    "fiscalDatetime": "20260910120000",
    "datetime": "2026-09-10T12:00:00",
    "cashDrawer": {"Sum": 1500.55, "Count": 3},
    "outputParameters": {"NumberOfChecks": 5, "CashBalance": 1500.55, "ResourcesFn": 120},
}


def envelope(result: Any, code: int = 0, description: str = "", success: bool = True) -> dict[str, Any]:
    return {"Result": result, "Code": code, "Description": description, "Success": success}


class MockServer:
    """Мок сервера ККМ: запоминает запросы и отдаёт заготовленные ответы."""

    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []
        self.bodies: dict[str, Any] = {}

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        path = request.url.path
        if request.content:
            self.bodies[path] = json.loads(request.content.decode("utf-8"))

        if path.endswith("/ping"):
            return httpx.Response(200, json=envelope({
                "product": "PrintService",
                "version": "1.27.0.1",
                "License": {"code": "ABC", "isEndUser": True, "expired": "2026-09-07T11:30:38.03+08:00"},
            }))
        if path.endswith("/kkt/list"):
            return httpx.Response(200, json=envelope([
                {"deviceName": "Emu", "DeviceType": 5},
                {"DeviceName": "Kassa2", "DeviceType": 1},
            ]))
        if path.endswith("/kkt"):
            return httpx.Response(200, json=envelope(None, code=2, description="Устройство не найдено", success=False))
        if path.endswith("/version"):
            return httpx.Response(200, json=envelope("1.27.0.1"))
        if path.endswith("/user/token"):
            return httpx.Response(200, json=envelope(
                {"TokenId": "token-42"}, description=request.headers.get("Authorization", "")
            ))
        if path.endswith("/queue"):
            return httpx.Response(200, json=envelope([
                {"DeviceName": "Emu", "DocId": "1", "Time": "2026-09-03T16:27:36"},
                {"DeviceName": "Emu", "DocId": "2", "Time": "2026-09-07T11:30:38.03+08:00"},
            ]))
        if path.endswith("/check/list"):
            return httpx.Response(200, json=envelope([
                {"DocId": "A1", "DocNumber": 3, "Date": "0001-01-01T00:00:00"},
            ]))
        if path.endswith("/task/status"):
            return httpx.Response(200, json=envelope(None, code=8, description="Документ не найден", success=False))
        if path.endswith("/slow"):
            time.sleep(5)
            return httpx.Response(200, json=envelope("done"))
        if path.endswith("/timeout"):
            raise httpx.ReadTimeout("timeout", request=request)
        if path.endswith("/refused"):
            raise httpx.ConnectError("сервер недоступен", request=request)
        if path.endswith("/denied"):
            return httpx.Response(401, content=b"")
        return httpx.Response(200, json=envelope(FISCAL_RESULT))


def connector(server: MockServer) -> SkkmConnector:
    kkm = SkkmConnector()
    kkm._http._client = httpx.Client(transport=httpx.MockTransport(server.handle), timeout=None)
    kkm.Host = "127.0.0.1"
    kkm.Port = 4398
    kkm.DeviceName = "Emu"
    return kkm


class TransportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MockServer()
        self.kkm = connector(self.server)

    def tearDown(self) -> None:
        self.kkm.Dispose()

    def test_ping_reads_camel_case_fields(self) -> None:
        self.kkm.Ping()
        self.assertTrue(self.kkm.Ok)
        self.assertEqual(self.kkm.LastResult["product"], "PrintService")
        self.assertEqual(self.server.requests[-1].url.path, "/PrintService/api/v4/ping")

    def test_device_list_is_case_insensitive(self) -> None:
        self.kkm.GetDeviceList()
        self.assertEqual([device.DeviceName for device in self.kkm.Devices], ["Emu", "Kassa2"])

    def test_headers_and_content_type(self) -> None:
        self.kkm.Token = "api-key-1"
        self.kkm.TerminalId = "T-1"
        self.kkm.OpenShift()
        request = self.server.requests[-1]
        self.assertEqual(request.headers.get("api_key"), "api-key-1")
        self.assertEqual(request.headers.get("TerminalId"), "T-1")
        self.assertEqual(request.headers.get("Content-Type"), "application/json; charset=utf-8")

    def test_basic_auth_only_for_token_request(self) -> None:
        self.kkm.GetUserToken()
        self.assertTrue(self.kkm.ErrorDescription.startswith("Basic "))
        self.assertEqual(self.kkm.Token, "token-42")

    def test_missing_device_is_server_error(self) -> None:
        self.kkm.Connect()
        self.assertFalse(self.kkm.Ok)
        self.assertEqual(self.kkm.ErrorCode, 2)
        self.assertEqual(self.kkm.ErrorDescription, "Устройство не найдено")

    def test_wrong_document_id_is_server_error(self) -> None:
        self.kkm.DocumentId = "нет-такого"
        self.kkm.GetTaskStatus()
        self.assertFalse(self.kkm.Ok)
        self.assertEqual(self.kkm.ErrorCode, 8)
        self.assertIsNone(self.kkm.TaskStatus)

    def test_unreachable_server(self) -> None:
        self.kkm._get("refused")
        self.assertEqual(self.kkm.ErrorCode, -1)
        self.assertIn("Ошибка соединения", self.kkm.ErrorDescription)

    def test_timeout(self) -> None:
        self.kkm._get("timeout")
        self.assertEqual(self.kkm.ErrorCode, -2)
        self.assertEqual(self.kkm.ErrorDescription, "Превышено время ожидания ответа сервера")

    def test_cancel_from_other_thread(self) -> None:
        started = time.monotonic()
        threading.Timer(0.3, self.kkm.Cancel).start()
        self.kkm._get("slow")
        self.assertEqual(self.kkm.ErrorCode, -3)
        self.assertEqual(self.kkm.ErrorDescription, "Запрос отменён")
        self.assertLess(time.monotonic() - started, 2)

    def test_http_401_message(self) -> None:
        self.kkm._get("denied")
        self.assertIn("Ошибка авторизации", self.kkm.ErrorDescription)

    def test_empty_host(self) -> None:
        self.kkm.Host = ""
        self.kkm.Ping()
        self.assertEqual(self.kkm.ErrorDescription, "Укажите Host и Port сервера ККМ.")

    def test_disposed_connector(self) -> None:
        self.kkm.Dispose()
        self.kkm.Ping()
        self.assertEqual(self.kkm.ErrorDescription, "Коннектор закрыт. Создайте новый SkkmConnector.")


class SerializationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MockServer()
        self.kkm = connector(self.server)
        self.kkm.Cashier = Cashier(Name="Иванов А.И.", Vatin="7722345678")
        self.kkm.NewRequest()
        self.kkm.PaymentType = CheckType.Sale
        self.kkm.TaxVariant = TaxSystem.ЕНВД
        self.kkm.Positions.append(
            FiscalLine(
                Name="Вода",
                Quantity=Decimal("2"),
                Price=Decimal("30.50"),
                Sum=Decimal("61"),
                Tax="20",
                TaxSum=Decimal("10.17"),
            )
        )
        self.kkm.Payments = Payments(Cash=Decimal("61"))
        self.kkm.PrintCheck()
        self.body: dict[str, Any] = self.server.bodies["/PrintService/api/v4/check"]

    def tearDown(self) -> None:
        self.kkm.Dispose()

    def test_property_order(self) -> None:
        self.assertEqual(list(self.body)[:2], ["DeviceName", "Cashier"])

    def test_none_is_not_serialized(self) -> None:
        self.assertNotIn("DocId", self.body)

    def test_json_property_names(self) -> None:
        fiscal = self.body["Positions"][0]["FiscalString"]
        self.assertEqual(fiscal["PriceWithDiscount"], 30.50)
        self.assertEqual(fiscal["SumWithDiscount"], 61)
        self.assertNotIn("Price", fiscal)

    def test_enums_are_numbers(self) -> None:
        self.assertEqual(self.body["PaymentType"], int(CheckType.Sale))
        self.assertEqual(self.body["TaxVariant"], int(TaxSystem.ЕНВД))

    def test_cyrillic_is_not_escaped(self) -> None:
        self.assertIn("Иванов", self.server.requests[-1].content.decode("utf-8"))

    def test_fiscal_result_fills_flat_properties(self) -> None:
        self.assertEqual(self.kkm.FiscalSign, "1234567890")
        self.assertEqual(self.kkm.DocumentId, "0AC0B2E1")
        self.assertEqual(self.kkm.ShiftNumber, 7)
        self.assertEqual(self.kkm.CheckNumber, 42)
        self.assertEqual(self.kkm.CheckNumberInShift, 5)
        self.assertEqual(self.kkm.CashBalance, Decimal("1500.55"))
        self.assertEqual(self.kkm.FnDaysResources, 120)


class ParsingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MockServer()
        self.kkm = connector(self.server)

    def tearDown(self) -> None:
        self.kkm.Dispose()

    def test_two_date_formats(self) -> None:
        self.kkm.GetQueue()
        self.assertEqual(self.kkm.Queue[0].Time.hour, 16)
        self.assertEqual(self.kkm.Queue[1].Time.hour, 11)

    def test_empty_date_is_min_value(self) -> None:
        self.kkm.ShiftNumber = 0
        self.kkm.GetCheckList()
        self.assertEqual(self.kkm.Checks[0].Date.year, 1)

    def test_period_in_query(self) -> None:
        self.kkm.GetCheckList()
        query = str(self.server.requests[-1].url)
        self.assertIn("from=", query)
        self.assertIn("to=", query)

    def test_string_result(self) -> None:
        self.kkm.GetVersion()
        self.assertEqual(self.kkm.ServerVersion, "1.27.0.1")

    def test_timeout_property_reaches_request(self) -> None:
        self.kkm.Timeout = timedelta(seconds=5)
        self.kkm.Ping()
        timeout: Optional[Any] = self.server.requests[-1].extensions.get("timeout")
        self.assertIsNotNone(timeout)


class SlipTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = MockServer()
        self.kkm = connector(self.server)

    def tearDown(self) -> None:
        self.kkm.Dispose()

    def test_slip_markup(self) -> None:
        self.kkm.TextForPrint = "[center,bold]Заголовок\n[line]\nОбычный текст\n[QR,center]https://rbsoft.ru"
        self.kkm.PrintSlip()
        positions = self.server.bodies["/PrintService/api/v4/slip"]["Positions"]
        self.assertEqual(positions[0]["TextString"]["Text"], "Заголовок")
        self.assertEqual(positions[0]["TextString"]["Font"], "Bold")
        self.assertEqual(positions[0]["TextString"]["Alignment"], "center")
        self.assertIn("SeparatorLine", positions[1])
        self.assertEqual(positions[2]["TextString"]["Text"], "Обычный текст")
        self.assertEqual(positions[3]["Barcode"]["Type"], "QR")
        self.assertEqual(positions[3]["Barcode"]["Value"], "https://rbsoft.ru")


class ProxyTests(unittest.TestCase):
    def test_loopback_bypasses_system_proxy(self) -> None:
        for host in ("localhost", "LOCALHOST", "127.0.0.1", "::1", "[::1]"):
            with self.subTest(host=host):
                self.assertFalse(uses_system_proxy(host))

    def test_remote_host_follows_system_exceptions(self) -> None:
        with mock.patch("urllib.request.proxy_bypass", return_value=True):
            self.assertFalse(uses_system_proxy("kassa.example"))
        with mock.patch("urllib.request.proxy_bypass", return_value=False):
            self.assertTrue(uses_system_proxy("kassa.example"))

    def test_localhost_client_ignores_system_proxy(self) -> None:
        transport = KkmTransport()
        self.assertFalse(transport._ensure_client().trust_env)
        transport.Dispose()


class AllMethodsTests(unittest.TestCase):
    """Каждый метод коннектора должен отработать на типовом ответе сервера."""

    SAMPLE_RESULT = {
        "docId": "A1",
        "fiscalSign": "FP",
        "shiftNumber": 1,
        "fiscalNumber": 2,
        "DeviceName": "Emu",
        "Status": {"LineLength": 42, "ShiftNumber": 1, "DocNumber": 2},
        "Device": {"LineLength": 42},
        "Fn": {"SaleLocation": "Офис"},
        "Counters": {"Sales": {"Sum": 10.5}},
        "TokenId": "t",
        "LineLength": 42,
        "LineLengthPixels": 576,
        "Sum": 5,
        "Guid": "G",
        "History": [{"Time": "2026-09-01T10:00:00", "State": 1, "Description": "ok"}],
    }

    def handle(self, request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path.endswith(("list", "queue", "/history", "/related")):
            result: Any = [self.SAMPLE_RESULT]
        elif "fiscalSign" in path or path.endswith(("/tlv", "version")):
            result = "строковый результат"
        else:
            result = self.SAMPLE_RESULT
        return httpx.Response(200, json=envelope(result))

    def test_every_method_runs(self) -> None:
        kkm = SkkmConnector()
        kkm._http._client = httpx.Client(transport=httpx.MockTransport(self.handle), timeout=None)
        kkm.DeviceName = "Emu"
        kkm.DocumentId = "A1"
        kkm.QueueTaskId = "Q1"
        kkm.TemplateName = "T1"
        kkm.PictureId = "P1"
        kkm.UserId = "U1"
        kkm.PoolName = "Pool"
        kkm.MarkingCodes.append("code")

        skip = {"Cancel", "Dispose", "NewRequest"}
        names = sorted(
            name
            for name in dir(kkm)
            if not name.startswith("_") and callable(getattr(kkm, name)) and name not in skip
        )
        self.assertGreaterEqual(len(names), 100)

        for name in names:
            with self.subTest(method=name):
                getattr(kkm, name)()
                self.assertTrue(kkm.Ok, f"{name}: {kkm.ErrorCode} {kkm.ErrorDescription}")
        kkm.Dispose()


class ContextManagerTests(unittest.TestCase):
    def test_dispose_on_exit(self) -> None:
        server = MockServer()
        with connector(server) as kkm:
            kkm.Ping()
            self.assertTrue(kkm.Ok)
        kkm.Ping()
        self.assertEqual(kkm.ErrorDescription, "Коннектор закрыт. Создайте новый SkkmConnector.")


if __name__ == "__main__":
    unittest.main()
