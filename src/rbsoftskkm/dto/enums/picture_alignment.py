from __future__ import annotations

from enum import IntEnum


class PictureAlignment(IntEnum):
    """Выравнивание изображения при печати или загрузке в ККТ:

    Left - По левому краю

    Center - По центру

    Right - По правому краю
    """

    #: По левому краю.
    Left = 1

    #: По центру.
    Center = 2

    #: По правому краю.
    Right = 3
