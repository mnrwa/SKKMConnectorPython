from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.enums.electronic_payment_method import ElectronicPaymentMethod


@dataclass
class ElectronicPayment:
    """Сведения об одной безналичной оплате (тег 1234 и связанные):

    Amount - Сумма оплаты безналичными

    PaymentMethod - Признак способа оплаты. Используйте enum ElectronicPaymentMethod

    Identifiers - Идентификаторы безналичной оплаты

    AdditionalInformation - Дополнительные сведения
    """

    #: Сумма оплаты безналичными.
    Amount: Decimal = Decimal("0")

    #: Признак способа оплаты безналичными. Используйте enum ElectronicPaymentMethod.
    PaymentMethod: Optional[ElectronicPaymentMethod] = None

    #: Идентификаторы безналичной оплаты.
    Identifiers: Optional[str] = None

    #: Дополнительные сведения о безналичной оплате.
    AdditionalInformation: Optional[str] = None
