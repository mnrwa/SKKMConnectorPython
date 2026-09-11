from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.text_string import TextString as _TextString
from rbsoftskkm.dto.positions.barcode_line import BarcodeLine
from rbsoftskkm.dto.positions.picture_line import PictureLine
from rbsoftskkm.dto.positions.separator_line import SeparatorLine as _SeparatorLine


@dataclass
class DocPosition:
    """Строка нефискального документа"""

    #: Печать текстовой строки
    TextString: Optional[_TextString] = None

    #: Печать штрихкода
    Barcode: Optional[BarcodeLine] = None

    #: Печать картинки (Base64)
    Picture: Optional[PictureLine] = None

    #: Горизонтальная разделительная линия на всю ширину чека
    SeparatorLine: Optional[_SeparatorLine] = None
