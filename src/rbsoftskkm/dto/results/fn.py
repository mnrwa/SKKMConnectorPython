from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from rbsoftskkm.dto.results.fn_modes import FnModes
from rbsoftskkm.dto.results.ofd import Ofd as _Ofd
from rbsoftskkm.dto.results.warnings import Warnings as _Warnings


@dataclass
class Fn:
    """Описание фискального накопителя"""

    #: Количество проведённых фискализаций
    FiscalizationsCount: int = 0

    #: Дата и время последней фискализации.
    FiscalizationDateTime: datetime = datetime.min

    #: Регистрационный номер ККТ (РНМ).
    RnNumber: Optional[str] = None

    #: Адрес сайта ФНС, напечатанный на чеке.
    FnsUrl: Optional[str] = None

    #: Email отправителя электронных чеков.
    SenderEmail: Optional[str] = None

    #: Код систем налогообложения
    TaxVariant: int = 0

    #: Код причины перерегистрации / изменения параметров.
    ReasonCode: int = 0

    #: Версия ФФД
    FfdVersion: Optional[str] = None

    #: Заводской номер фискального накопителя.
    SerialNumber: Optional[str] = None

    #: Наименование организации
    OrganizationName: Optional[str] = None

    #: ИНН владельца ККТ.
    Vatin: Optional[str] = None

    #: Дата окончания срока действия ФН.
    ValidityDate: datetime = datetime.min

    #: Адрес расчётов
    SaleAddress: Optional[str] = None

    #: Место расчётов
    SaleLocation: Optional[str] = None

    #: Признак агента (тег 1057).
    SignOfAgent: int = 0

    #: Номер автомата
    AutomaticNumber: Optional[str] = None

    #: Оператор фискальных данных
    Ofd: Optional[_Ofd] = None

    #: Предупреждения ФН
    Warnings: Optional[_Warnings] = None

    #: Разрешённые режимы работы ККТ
    Modes: Optional[FnModes] = None
