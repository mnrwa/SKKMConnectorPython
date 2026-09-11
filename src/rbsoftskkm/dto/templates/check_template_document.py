from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from rbsoftskkm.dto.correction_data import CorrectionData as _CorrectionData
from rbsoftskkm.dto.customer import Customer as _Customer
from rbsoftskkm.dto.electronic_payment import ElectronicPayment
from rbsoftskkm.dto.enums.check_time_zone import CheckTimeZone
from rbsoftskkm.dto.enums.check_type import CheckType
from rbsoftskkm.dto.enums.tax_system import TaxSystem
from rbsoftskkm.dto.operational_attribute import OperationalAttribute as _OperationalAttribute
from rbsoftskkm.dto.payments import Payments as _Payments
from rbsoftskkm.dto.positions.industry import Industry
from rbsoftskkm.dto.positions.position import Position
from rbsoftskkm.dto.results.check_item import CheckItem
from rbsoftskkm.dto.user_attribute import UserAttribute as _UserAttribute


@dataclass
class CheckTemplateDocument:
    """Документ шаблона чека: тип чека, СНО, оплаты (Payments), позиции,
    покупатель, агент и прочие реквизиты — по аналогии с обычным чеком.
    """

    #: Тип чека
    PaymentType: CheckType = CheckType.Text

    #: Система налогообложения
    TaxVariant: TaxSystem = TaxSystem.ОСН

    #: Часовая зона.
    TimeZone: Optional[CheckTimeZone] = None

    #: Признак расчёта в сети Интернет.
    OperationOnline: bool = False

    #: Адрес электронной почты отправителя чека.
    SenderEmail: str = ""

    #: Адрес проведения расчётов.
    SaleAddress: str = ""

    #: Место проведения расчётов.
    SaleLocation: str = ""

    #: Формирование чека только в электронном виде.
    Electronically: bool = False

    #: Покупатель.
    Customer: Optional[_Customer] = None

    #: Позиции чека
    Positions: list[Position] = field(default_factory=list)

    #: Строки шаблона
    CheckItems: list[CheckItem] = field(default_factory=list)

    #: Оплаты чека.
    Payments: Optional[_Payments] = None

    #: Электронные платежи.
    ElectronicPayments: list[ElectronicPayment] = field(default_factory=list)

    #: Данные коррекции
    CorrectionData: Optional[_CorrectionData] = None

    #: Отраслевой реквизит чека
    IndustryAttribute: Optional[Industry] = None

    #: Дополнительный реквизит пользователя
    UserAttribute: Optional[_UserAttribute] = None

    #: Операционный реквизит чека
    OperationalAttribute: Optional[_OperationalAttribute] = None

    #: Дополнительный реквизит чека (БСО), тег 1192
    AdditionalAttribute: str = ""
