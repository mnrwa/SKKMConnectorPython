"""Основа коннектора: транспорт, отмена запроса и освобождение соединения."""

from __future__ import annotations

import threading
from typing import Optional

from rbsoftskkm.data.kkm_transport import CancelToken, KkmTransport


class SkkmConnectorBase:
    """Держатель HTTP-соединения. Один экземпляр — одна сессия."""

    def __init__(self) -> None:
        self._http = KkmTransport()
        self._call_lock = threading.Lock()
        self._call_cancel: Optional[CancelToken] = None
        self._disposed = False

    def Cancel(self) -> None:
        """Отменяет текущий HTTP-запрос к серверу ККМ."""
        with self._call_lock:
            token = self._call_cancel
        if token is not None:
            token.cancel()

    def Dispose(self) -> None:
        """Освобождает HTTP-соединение с сервером ККМ.

        После этого экземпляр использовать нельзя — создайте новый, если снова
        нужен доступ к кассе.
        """
        if self._disposed:
            return
        self._disposed = True
        self.Cancel()
        self._http.Dispose()

    def __enter__(self) -> "SkkmConnectorBase":
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.Dispose()
