from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class DocDataPayments:
    """Разбивка суммы операций по видам оплаты"""

    #: Общая сумма оплат.
    Sum: Decimal = Decimal("0")

    #: Наличные
    Cash: Decimal = Decimal("0")

    #: Безналичные
    Electronically: Decimal = Decimal("0")

    #: Аванс (предоплата).
    Prepaid: Decimal = Decimal("0")

    #: Кредит (постоплата).
    Credit: Decimal = Decimal("0")

    #: Встречные предоставления (бартер).
    Barter: Decimal = Decimal("0")
