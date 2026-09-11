from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Payments:
    """Суммы оплаты по способам расчёта:

    Cash - Наличными

    ElectronicPayment - Безналичными

    AdvancePayment - Предоплатой (зачётом аванса)

    Credit - Постоплатой (в кредит)

    CashProvision - Встречным предоставлением

    Заполните одну или несколько сумм; итог должен соответствовать сумме позиций чека.
    """

    #: Сумма наличной оплаты.
    Cash: Decimal = Decimal("0")

    #: Сумма безналичными средствами.
    ElectronicPayment: Decimal = Decimal("0")

    #: Сумма предоплатой (зачётом аванса).
    AdvancePayment: Decimal = Decimal("0")

    #: Сумма постоплатой (в кредит).
    Credit: Decimal = Decimal("0")

    #: Сумма встречным предоставлением.
    CashProvision: Decimal = Decimal("0")
