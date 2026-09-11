from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProxyConfig:
    """Настройки прокси-сервера:

    IsUseProxy - Включить прокси для общих запросов

    IsUseProxyService - Использовать прокси для службы печати

    IsUseProxyMarking - Использовать прокси для запросов маркировки

    IpAddress - IP-адрес или DNS-имя прокси-сервера

    Port - TCP-порт прокси-сервера

    Name - Логин для авторизации на прокси

    Password - Пароль для авторизации на прокси
    """

    #: true — использовать прокси для общих запросов сервера ККМ.
    IsUseProxy: bool = False

    #: true — использовать прокси для службы печати.
    IsUseProxyService: bool = False

    #: true — использовать прокси для запросов маркировки (ИСМ и связанные).
    IsUseProxyMarking: bool = False

    #: IP-адрес или DNS-имя прокси-сервера.
    IpAddress: str = ""

    #: TCP-порт прокси-сервера.
    Port: int = 0

    #: Логин для авторизации на прокси (если требуется).
    Name: str = ""

    #: Пароль для авторизации на прокси (если требуется).
    Password: str = ""
