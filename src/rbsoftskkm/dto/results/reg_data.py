from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class RegData:
    """Счётчик скидок или надбавок"""

    #: Количество операций (скидок или надбавок).
    Count: int = 0

    #: Сумма операций.
    Sum: Decimal = Decimal("0")
