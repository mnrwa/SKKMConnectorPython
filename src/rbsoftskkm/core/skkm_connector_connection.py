"""Параметры подключения к серверу ККМ и общие настройки сессии."""

from __future__ import annotations

from datetime import timedelta
from typing import Optional

from rbsoftskkm.core.skkm_connector_state import SkkmConnectorState
from rbsoftskkm.dto.admin.device_settings import DeviceSettings
from rbsoftskkm.dto.admin.service_settings import ServiceSettings
from rbsoftskkm.dto.admin.service_user import ServiceUser
from rbsoftskkm.dto.cashier import Cashier
from rbsoftskkm.dto.fiscalization.fiscalization_parameters import FiscalizationParameters
from rbsoftskkm.dto.templates.check_template_parameters import CheckTemplateParameters
from rbsoftskkm.dto.templates.template_parameters import TemplateParameters


class SkkmConnectorConnection(SkkmConnectorState):
    """Подключение."""

    #: Хост сервера ККМ (IP или DNS). Можно менять между запросами, пока программа запущена.
    Host: str

    #: TCP-порт сервера ККМ. Можно менять между запросами, пока программа запущена.
    Port: int

    #: HTTPS вместо HTTP.
    UseHttps: bool

    #: Таймаут запроса к серверу ККМ. По умолчанию 60 секунд.
    Timeout: timedelta

    #: Токен авторизации (заголовок api_key). Можно менять между запросами, пока программа запущена.
    Token: str

    #: Идентификатор терминала.
    TerminalId: str

    #: Имя устройства.
    DeviceName: str

    #: Сведения о кассире (продавце). Создайте объект Cashier (Name, Vatin).
    Cashier: Optional[Cashier]

    #: Логин для Basic Auth при получении токена. По умолчанию Admin.
    AuthUserName: str

    #: Пароль для Basic Auth при получении токена. По умолчанию Admin.
    AuthPassword: str

    #: Имя пула устройств.
    PoolName: str

    #: Тип отчёта для списка Z-отчётов.
    ReportType: int

    #: Идентификатор задания в очереди печати.
    QueueTaskId: str

    #: Имя картинки или шаблона.
    PictureId: str

    #: Имя шаблона печати или чека.
    TemplateName: str

    #: Идентификатор пользователя сервера ККМ.
    UserId: str

    #: Номер ФН.
    FnNumber: str

    #: Коды маркировки для проверки.
    MarkingCodes: list[str]

    #: Настройки кассы для добавления или изменения.
    #: Создайте объект DeviceSettings и заполните нужные поля.
    DeviceSettings: Optional[DeviceSettings]

    #: Настройки службы печати. Создайте объект ServiceSettings
    #: (WcfServicePort, WebServicePort, ServiceTimeOut, ProxyServerSettings, MaxQueueSize, RepeatPrintingOnError).
    ServiceSettings: Optional[ServiceSettings]

    #: Пользователь сервера ККМ. Создайте объект ServiceUser
    #: (Id, UserName, FullName, Vatin, Role, TokenId, Password).
    ServiceUser: Optional[ServiceUser]

    #: Параметры шаблона печати. Создайте объект TemplateParameters (Name, Type, TemplateItems).
    TemplateParameters: Optional[TemplateParameters]

    #: Параметры шаблона чека. Создайте объект CheckTemplateParameters (Name, Document).
    CheckTemplateParameters: Optional[CheckTemplateParameters]

    #: Параметры фискализации / перерегистрации.
    #: Создайте объект FiscalizationParameters и заполните нужные поля.
    FiscalizationParameters: Optional[FiscalizationParameters]

    def __init__(self) -> None:
        super().__init__()
        self.Host = "localhost"
        self.Port = 4398
        self.UseHttps = False
        self.Timeout = timedelta(seconds=60)
        self.Token = ""
        self.TerminalId = ""
        self.DeviceName = ""
        self.Cashier = None
        self.AuthUserName = "Admin"
        self.AuthPassword = "Admin"
        self.PoolName = ""
        self.ReportType = 0
        self.QueueTaskId = ""
        self.PictureId = ""
        self.TemplateName = ""
        self.UserId = ""
        self.FnNumber = ""
        self.MarkingCodes = []
        self.DeviceSettings = None
        self.ServiceSettings = None
        self.ServiceUser = None
        self.TemplateParameters = None
        self.CheckTemplateParameters = None
        self.FiscalizationParameters = None
