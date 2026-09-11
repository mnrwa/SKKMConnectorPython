from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.results.cash_drawer import CashDrawer as _CashDrawer
from rbsoftskkm.dto.results.shift_counters import ShiftCounters
from rbsoftskkm.dto.results.shift_income import ShiftIncome as _ShiftIncome


@dataclass
class ResShiftTotal:
    """Итоги текущей кассовой смены"""

    #: Номер смены.
    ShiftNumber: float = 0.0

    #: Денежный ящик: остаток наличных и число операций.
    CashDrawer: Optional[_CashDrawer] = None

    #: Внесения за смену.
    ShiftIncome: Optional[_ShiftIncome] = None

    #: Выемки за смену.
    ShiftOutcome: Optional[_ShiftIncome] = None

    #: Счетчики фискальных операций за смену
    Counters: Optional[ShiftCounters] = None
