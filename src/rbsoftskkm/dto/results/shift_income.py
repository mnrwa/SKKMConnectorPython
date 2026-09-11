from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ShiftIncome:
    """Итог внесений или выемок за смену"""

    #: Количество операций
    Count: int = 0

    #: Сумма операций.
    Sum: Decimal = Decimal("0")
