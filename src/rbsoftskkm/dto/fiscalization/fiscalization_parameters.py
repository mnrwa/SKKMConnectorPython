from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.cashier import Cashier as _Cashier
from rbsoftskkm.dto.enums.fiscalization_reason_code import FiscalizationReasonCode


@dataclass
class FiscalizationParameters:
    """Параметры фискализации / перерегистрации ККТ.

    Регистрационные данные:

    DeviceName - Имя кассы на сервере ККМ

    Cashier - Кассир (объект Cashier: Name, Vatin)

    RnNumber - Регистрационный номер ККТ (РНМ)

    TaxationSystems - Системы налогообложения через запятую (коды 0–5, например "0,1,2")

    Vatin - ИНН организации

    CompanyName - Наименование организации

    Fn - Заводской номер фискального накопителя

    ФФД и коды изменения сведений:

    FfdVersionKkt - Версия ФФД ККТ (например "1.05", "1.2")

    FfdVersionFn - Версия ФФД ФН

    RegistrationLabelCodes - Коды причин изменения сведений о ККТ (например "3.1")

    ОФД и отправитель:

    OfdAddress / OfdPort - Адрес и порт сервера ОФД

    OfdVatin / OfdName - ИНН и наименование ОФД

    SenderEmail - Email отправителя чеков

    ReasonCode - Причина перерегистрации. Используйте enum FiscalizationReasonCode

    ИСМ, ФНС, автоматы, агенты:

    IsmHost / IsmPort - Хост и порт ИСМ (для маркировки)

    FnsUrl - Адрес сайта ФНС (например "nalog.ru")

    AutomaticNumber - Номер автоматического устройства для расчётов

    AgentTypes - Признаки агента через запятую (коды типов агента)

    Признаки режимов применения ККТ (true / false):

    IsBsoSign - АС БСО

    IsMarking - Маркированные товары

    IsPawnshop - Ломбард

    IsAssurance - Страхование

    IsAutomatic - Автоматический режим

    IsVending - Торговый автомат

    IsAutomaticPrinter - Принтер в автомате

    IsOnline - Только интернет-расчёты

    IsLottery - Лотереи

    IsGambling - Азартные игры

    IsExcisable - Подакцизные товары

    IsService - Услуги

    IsEncrypted - Шифрование данных

    IsOffline - Автономный режим (без ОФД)

    IsCateringServices - Общественное питание

    IsWholesaleTrade - Оптовая торговля

    Адрес расчётов:

    SaleAddress - Адрес места расчётов

    SaleLocation - Место расчётов (например "Офис", "Торговый зал")
    """

    #: Имя кассы на сервере ККМ. Если пусто — берётся из kkm.DeviceName.
    DeviceName: str = ""

    #: Кассир, выполняющий регистрацию. Создайте объект Cashier (Name, Vatin).
    #: Если не задан — берётся из kkm.Cashier.
    Cashier: Optional[_Cashier] = None

    #: Регистрационный номер ККТ (РНМ), выданный при регистрации в ФНС.
    RnNumber: str = ""

    #: Применяемые системы налогообложения — коды через запятую
    #: (0 — ОСН, 1 — УСН доход, 2 — УСН доход−расход, 3 — ЕНВД, 4 — ЕСХН, 5 — ПСН).
    #: Пример: "0,1,2".
    TaxationSystems: str = ""

    #: ИНН организации-пользователя ККТ.
    Vatin: str = ""

    #: Наименование организации-пользователя ККТ.
    CompanyName: str = ""

    #: Заводской номер фискального накопителя (ФН).
    Fn: str = ""

    #: Версия формата фискальных документов ККТ. Пример: "1.2", "1.05".
    FfdVersionKkt: str = ""

    #: Версия формата фискальных документов ФН. Пример: "1.2".
    FfdVersionFn: str = ""

    #: Коды причин изменения сведений о ККТ (через запятую или точку, по формату сервера).
    #: Пример: "3.1".
    RegistrationLabelCodes: str = ""

    #: DNS-имя или IP-адрес сервера ОФД.
    OfdAddress: str = ""

    #: TCP-порт сервера ОФД.
    OfdPort: int = 0

    #: Номер автоматического устройства для расчётов (для автоматов / АС).
    AutomaticNumber: str = ""

    #: Адрес электронной почты отправителя чека (тег 1117).
    SenderEmail: str = ""

    #: Причина перерегистрации ККТ. Используйте enum FiscalizationReasonCode.
    #: Для первичной регистрации может не требоваться.
    ReasonCode: Optional[FiscalizationReasonCode] = None

    #: Хост ИСМ (информационная система маркировки), если используется маркировка.
    IsmHost: str = ""

    #: Порт ИСМ.
    IsmPort: int = 0

    #: Адрес сайта ФНС. Пример: "nalog.ru".
    FnsUrl: str = ""

    #: ИНН оператора фискальных данных (ОФД).
    OfdVatin: str = ""

    #: Наименование оператора фискальных данных (ОФД).
    OfdName: str = ""

    #: Признаки агента — числовые коды через запятую (см. AgentType).
    AgentTypes: str = ""

    #: true — ККТ применяется для формирования АС БСО.
    IsBsoSign: bool = False

    #: true — ККТ применяется при продаже маркированных товаров.
    IsMarking: bool = False

    #: true — ККТ применяется при осуществлении ломбардной деятельности.
    IsPawnshop: bool = False

    #: true — ККТ применяется при осуществлении страховой деятельности.
    IsAssurance: bool = False

    #: true — ККТ применяется в автоматическом режиме.
    IsAutomatic: bool = False

    #: true — ККТ применяется в составе торгового автомата (вендинг).
    IsVending: bool = False

    #: true — в автоматическом устройстве установлен принтер чеков.
    IsAutomaticPrinter: bool = False

    #: true — расчёты ведутся только в сети Интернет (без выдачи бумажного чека покупателю на месте).
    IsOnline: bool = False

    #: true — ККТ применяется при проведении лотерей.
    IsLottery: bool = False

    #: true — ККТ применяется при проведении азартных игр.
    IsGambling: bool = False

    #: true — ККТ применяется при продаже подакцизных товаров.
    IsExcisable: bool = False

    #: true — ККТ применяется при оказании услуг.
    IsService: bool = False

    #: true — данные в ФН шифруются.
    IsEncrypted: bool = False

    #: true — автономный режим (без передачи данных в ОФД).
    IsOffline: bool = False

    #: true — ККТ применяется при оказании услуг общественного питания.
    IsCateringServices: bool = False

    #: true — ККТ применяется при оптовой торговле.
    IsWholesaleTrade: bool = False

    #: Адрес места осуществления расчётов (улица, дом и т.п.).
    SaleAddress: str = ""

    #: Место расчётов (краткое наименование: офис, торговый зал, павильон и т.п.).
    SaleLocation: str = ""
