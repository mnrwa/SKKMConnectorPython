from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.results.shift_counters import ShiftCounters


@dataclass
class OverallTotals:
    """Необнуляемые счётчики ККТ."""

    #: Счётчики фискальных операций.
    Counters: Optional[ShiftCounters] = None
