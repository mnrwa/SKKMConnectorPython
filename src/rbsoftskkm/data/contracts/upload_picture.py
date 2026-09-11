from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class UploadPicture:
    """Тело запроса загрузки картинки."""

    #: Имя кассы
    DeviceName: Optional[str] = None

    #: Изображение в формате Base64 (BMP)
    Base64: Optional[str] = None

    #: Имя картинки на сервере
    PictureName: Optional[str] = None

    #: Выравнивание: 1 - слева, 2 - по центру, 3 - справа
    Alignment: int = 2
