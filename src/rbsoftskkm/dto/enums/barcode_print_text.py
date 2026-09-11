from __future__ import annotations

from enum import IntEnum


class BarcodePrintText(IntEnum):
    """Способ печати текста штрихкода (для одномерных):

    None - Не печатать

    Below - Снизу

    Above - Сверху

    AboveAndBelow - Сверху и снизу
    """

    #: Не печатать.
    None_ = 0

    #: Печатать снизу.
    Below = 1

    #: Печатать сверху.
    Above = 2

    #: Печатать сверху и снизу.
    AboveAndBelow = 3
