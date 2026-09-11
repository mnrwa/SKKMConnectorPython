from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.connection_method import ConnectionMethod
from rbsoftskkm.dto.enums.device_type import DeviceType as _DeviceType


@dataclass
class DeviceSettings:
    """Настройки кассы на сервере ККМ:

    DeviceName - Имя кассы

    DeviceType - Тип драйвера ККТ. Используйте enum DeviceType

    Available - Доступность устройства для печати (true — доступно)

    MethodConnection - Способ связи с ККТ. Используйте enum ConnectionMethod

    PortNumber - Номер COM-порта (для MethodConnection = Com)

    BaudRate - Скорость COM-порта (например 9600, 115200)

    IpAddress - IP-адрес ККТ (для MethodConnection = TcpIp)

    TcpPort - TCP-порт ККТ (для MethodConnection = TcpIp)

    Password - Пароль пользователя ККТ

    AccessPassword - Пароль администратора / доступ к настройкам ККТ

    SerialNumber - Заводской номер ККТ

    Vatin - ИНН организации-пользователя ККТ

    OrganizationName - Наименование организации

    SaleAddress - Адрес места расчётов

    ClientSaleLocation - Место расчётов (офис, торговый зал и т.п.)

    Cashier - Имя кассира по умолчанию

    CashierVatin - ИНН кассира по умолчанию

    SenderEmail - Email отправителя чека

    TimeoutConnection - Таймаут соединения с ККТ, мс

    TimeoutWaitForPrinting - Таймаут ожидания завершения печати, мс

    OfdAddress - Адрес (хост) ОФД

    OfdPort - Порт ОФД

    Pool - Имя пула устройств (если касса входит в пул)

    TemplateSettingH1…H5 - Параметры шаблонов печати H1–H5
    """

    #: Имя кассы на сервере ККМ (уникальный идентификатор устройства).
    DeviceName: str = ""

    #: Тип драйвера ККТ. Используйте enum DeviceType.
    DeviceType: Optional[_DeviceType] = None

    #: true — устройство доступно для печати; false — недоступно.
    Available: bool = False

    #: Способ связи с ККТ. Используйте enum ConnectionMethod
    #: (Com — COM-порт, TcpIp — сеть).
    MethodConnection: ConnectionMethod = ConnectionMethod.Com

    #: Номер COM-порта. Используется при Com.
    PortNumber: int = 0

    #: Скорость COM-порта (бод). Пример: 9600, 115200.
    BaudRate: int = 0

    #: IP-адрес ККТ. Используется при TcpIp.
    IpAddress: str = ""

    #: TCP-порт ККТ. Используется при TcpIp.
    TcpPort: int = 0

    #: Пароль пользователя ККТ.
    Password: str = ""

    #: Пароль администратора / доступ к настройкам ККТ.
    AccessPassword: str = ""

    #: Заводской номер ККТ.
    SerialNumber: str = ""

    #: ИНН организации-пользователя ККТ.
    Vatin: str = ""

    #: Наименование организации.
    OrganizationName: str = ""

    #: Адрес места осуществления расчётов.
    SaleAddress: str = ""

    #: Место расчётов (краткое наименование: офис, торговый зал и т.п.).
    ClientSaleLocation: str = ""

    #: Имя кассира по умолчанию для этой кассы.
    Cashier: str = ""

    #: ИНН кассира по умолчанию.
    CashierVatin: str = ""

    #: Email отправителя чека (тег 1117).
    SenderEmail: str = ""

    #: Таймаут соединения с ККТ, миллисекунды.
    TimeoutConnection: int = 0

    #: Таймаут ожидания завершения печати, миллисекунды.
    TimeoutWaitForPrinting: int = 0

    #: DNS-имя или IP-адрес сервера ОФД.
    OfdAddress: str = ""

    #: TCP-порт сервера ОФД.
    OfdPort: int = 0

    #: Имя пула устройств, в который входит касса (если используется пул).
    Pool: str = ""

    #: Параметр шаблона печати H1.
    TemplateSettingH1: str = ""

    #: Параметр шаблона печати H2.
    TemplateSettingH2: str = ""

    #: Параметр шаблона печати H3.
    TemplateSettingH3: str = ""

    #: Параметр шаблона печати H4.
    TemplateSettingH4: str = ""

    #: Параметр шаблона печати H5.
    TemplateSettingH5: str = ""
