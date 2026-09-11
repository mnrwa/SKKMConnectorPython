from __future__ import annotations

from enum import IntEnum


class ShiftState(IntEnum):
    """Состояние кассовой смены:

    Closed - Смена закрыта

    Opened - Смена открыта

    Expired - Смена истекла (открыта более 24 часов)
    """

    #: Смена закрыта
    Closed = 1

    #: Смена открыта
    Opened = 2

    #: Смена истекла (открыта более 24 часов)
    Expired = 3
