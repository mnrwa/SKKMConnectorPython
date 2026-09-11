from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.shift_state import ShiftState as _ShiftState
from rbsoftskkm.dto.results.backlog import Backlog as _Backlog


@dataclass
class ResponseCurrentStatus:
    """Краткий статус смены и очереди ОФД"""

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер последнего фискального документа.
    CheckNumber: int = 0

    #: Состояние смены: 1 — закрыта, 2 — открыта, 3 — истекла.
    ShiftState: Optional[_ShiftState] = None

    #: Статус обмена данными с ОФД.
    Backlog: Optional[_Backlog] = None
