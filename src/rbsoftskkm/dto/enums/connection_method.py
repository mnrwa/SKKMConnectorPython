from __future__ import annotations

from enum import IntEnum


class ConnectionMethod(IntEnum):
    """Метод подключения устройства:

    Com - COM-порт

    TcpIp - TCP/IP
    """

    #: COM-порт.
    Com = 0

    #: TCP/IP.
    TcpIp = 1
