from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.api_position import ApiPosition
from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.dto.customer import Customer as _Customer
from rbsoftskkm.dto.electronic_payment import ElectronicPayment
from rbsoftskkm.dto.operational_attribute import OperationalAttribute as _OperationalAttribute
from rbsoftskkm.dto.payments import Payments as _Payments
from rbsoftskkm.dto.positions.agent import Agent
from rbsoftskkm.dto.positions.industry import Industry
from rbsoftskkm.dto.positions.vendor import Vendor as _Vendor
from rbsoftskkm.dto.user_attribute import UserAttribute as _UserAttribute


@dataclass
class CheckParameters(CheckbaseParameters):
    """Параметры для печати чека или чека коррекции 1.2"""

    #: Тип чека
    PaymentType: int = 0

    #: Код системы налогообложения
    TaxVariant: int = 0

    #: Сведения о покупателе (клиенте)
    Customer: Optional[_Customer] = None

    #: Место проведения расчетов
    SaleLocation: Optional[str] = None

    #: Адрес проведения расчетов
    SaleAddress: Optional[str] = None

    #: Адрес электронной почты отправителя чека
    SenderEmail: Optional[str] = None

    #: Признак применения ККТ при осуществлении расчета в безналичном порядке в сети «Интернет»
    OperationOnline: Optional[bool] = None

    #: Отраслевой реквизит чека
    IndustryAttribute: Optional[Industry] = None

    #: Дополнительный реквизит пользователя
    UserAttribute: Optional[_UserAttribute] = None

    #: Операционный реквизит чека
    OperationalAttribute: Optional[_OperationalAttribute] = None

    #: Сведения об оплате безналичными
    ElectronicPaymentInfo: Optional[list[ElectronicPayment]] = None

    #: Формирование чека только в электронном виде
    Electronically: bool = False

    #: Номер часовой зоны места расчётов.
    #: Если поле не указано, используется значение из поля «Часовая зона» в настройках ККТ.
    TimeZone: Optional[int] = None

    #: Текст для печати перед товарной частью
    TextBefore: Optional[str] = None

    #: Текст для печати после товарной части чека
    TextAfter: Optional[str] = None

    #: Дополнительный реквизит чека (БСО), тег 1192
    AdditionalAttribute: Optional[str] = None

    #: Признак агента
    AgentSign: Optional[int] = None

    #: Данные агента
    AgentData: Optional[Agent] = None

    #: Данные поставщика
    Vendor: Optional[_Vendor] = None

    #: Оплаты
    Payments: Optional[_Payments] = None

    #: Товары
    Positions: Optional[list[ApiPosition]] = None
