"""Коннектор Сервера ККМ."""

from __future__ import annotations

from rbsoftskkm.core.skkm_connector_api import SkkmConnectorApi


class SkkmConnector(SkkmConnectorApi):
    """Коннектор Сервера ККМ. Один экземпляр — одна сессия.

    Коннектор поддерживает протокол менеджера контекста, поэтому соединение
    закрывается само::

        with SkkmConnector() as kkm:
            kkm.Host = "localhost"
            kkm.DeviceName = "Emu"
            kkm.Ping()
    """

    def __enter__(self) -> "SkkmConnector":
        return self
