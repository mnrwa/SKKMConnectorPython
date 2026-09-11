from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.picture_alignment import PictureAlignment


@dataclass
class Picture:
    """Элемент списка изображений."""

    #: Название изображения.
    PictureName: Optional[str] = None

    #: Выравнивание изображения.
    Alignment: Optional[PictureAlignment] = None

    #: Изображение в Base64 (строка шаблона печати / печатной формы).
    PictureBase64: Optional[str] = None

    #: Ширина изображения при печати, в точках.
    Width: Optional[int] = None

    #: Высота изображения при печати, в точках.
    Height: Optional[int] = None
