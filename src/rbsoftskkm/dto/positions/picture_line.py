from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.picture_alignment import PictureAlignment
from rbsoftskkm.dto.positions.position import Position


@dataclass
class PictureLine(Position):
    """Изображение в чеке:

    Value - Картинка в Base64

    Alignment - Выравнивание. Используйте enum PictureAlignment

    Width / Height - Размер (при необходимости)
    """

    #: Изображение в Base64.
    Value: str = ""

    #: Выравнивание изображения. Используйте enum PictureAlignment.
    Alignment: PictureAlignment = PictureAlignment.Center

    #: Ширина изображения.
    Width: Optional[int] = None

    #: Высота изображения.
    Height: Optional[int] = None
