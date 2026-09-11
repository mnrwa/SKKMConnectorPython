from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.positions.position import Position


@dataclass
class TextLine(Position):
    """Текстовая строка чека:

    Text - Текст

    Font - Шрифт

    Alignment - Выравнивание
    """

    #: Текст строки
    Text: str = ""

    #: Шрифт
    Font: Optional[str] = None

    #: Выравнивание
    Alignment: Optional[str] = None
