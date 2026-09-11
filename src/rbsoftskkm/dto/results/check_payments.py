from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CheckPayments:
    """Оплаты из ответа сервера (Payments)"""

    #: Сумма наличной оплаты.
    Cash: Decimal = Decimal("0")

    #: Сумма безналичными средствами.
    Electronic: Decimal = Decimal("0")

    #: Сумма предоплатой (зачётом аванса).
    PrePaid: Decimal = Decimal("0")

    #: Сумма постоплатой (в кредит).
    Credit: Decimal = Decimal("0")

    #: Сумма встречным предоставлением.
    Barter: Decimal = Decimal("0")
