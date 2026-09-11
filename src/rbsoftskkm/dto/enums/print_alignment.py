from __future__ import annotations

from enum import IntEnum


class PrintAlignment(IntEnum):
    """Выравнивание строки или штрихкода при печати:

    Left - По левому краю

    Center - По центру

    Right - По правому краю

    Width - На всю ширину
    """

    #: По левому краю.
    Left = 0

    #: По центру.
    Center = 1

    #: По правому краю.
    Right = 2

    #: На всю ширину.
    Width = 3
