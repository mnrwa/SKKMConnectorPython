from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.admin.proxy_config import ProxyConfig


@dataclass
class ServiceSettings:
    """Настройки службы печати:

    WcfServicePort - TCP-порт WCF-службы сервера ККМ

    WebServicePort - TCP-порт веб-службы (HTTP API)

    ServiceTimeOut - Таймаут ожидания ответа службы

    ProxyServerSettings - Настройки прокси. Создайте объект ProxyConfig

    MaxQueueSize - Максимальное число заданий в очереди печати

    RepeatPrintingOnError - Повторять печать при ошибке (true / false)
    """

    #: TCP-порт WCF-службы сервера ККМ.
    WcfServicePort: int = 0

    #: TCP-порт веб-службы (HTTP API).
    WebServicePort: int = 0

    #: Таймаут ожидания ответа службы (строка в формате, ожидаемом сервером).
    ServiceTimeOut: str = ""

    #: Настройки прокси-сервера. Создайте объект ProxyConfig и заполните нужные поля.
    ProxyServerSettings: Optional[ProxyConfig] = None

    #: Максимальное число заданий в очереди печати.
    MaxQueueSize: int = 0

    #: true — повторять печать при ошибке; false — не повторять.
    RepeatPrintingOnError: bool = False
