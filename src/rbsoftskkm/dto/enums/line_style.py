from __future__ import annotations

from enum import IntEnum


class LineStyle(IntEnum):
    """Стиль разделительной линии:

    Solid - Сплошная линия (по умолчанию)

    Bold - Жирная линия

    Dashed - Штриховая линия

    Dotted - Пунктирная линия

    Double - Двойная линия
    """

    #: Сплошная линия (по умолчанию).
    Solid = 0

    #: Жирная линия.
    Bold = 1

    #: Штриховая линия.
    Dashed = 2

    #: Пунктирная линия.
    Dotted = 3

    #: Двойная линия.
    Double = 4
