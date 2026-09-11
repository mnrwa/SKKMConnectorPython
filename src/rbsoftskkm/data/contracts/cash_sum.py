from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CashSum:
    """Остаток наличных в денежном ящике."""

    #: Сумма наличных в денежном ящике
    Sum: Decimal = Decimal("0")
