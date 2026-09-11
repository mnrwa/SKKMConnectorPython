from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CashDrawer:
    """Состояние денежного ящика: сумма наличных и число операций."""

    #: Сумма наличных в ящике.
    Sum: Decimal = Decimal("0")

    #: Количество операций с наличными.
    Count: int = 0
