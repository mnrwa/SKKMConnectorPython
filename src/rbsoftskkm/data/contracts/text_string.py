from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TextString:
    """Печать текстовой строки в документе."""

    #: Строка с произвольным текстом
    Text: Optional[str] = None

    #: Шрифт строки: Normal, Bold, Small, Medium, Big, H1, H2, H3, H4, H5
    Font: Optional[str] = None

    #: Выравнивание: left, right, center, width
    Alignment: Optional[str] = None
