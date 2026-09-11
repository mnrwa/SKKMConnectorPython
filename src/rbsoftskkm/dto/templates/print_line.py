from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.print_alignment import PrintAlignment
from rbsoftskkm.dto.enums.print_font import PrintFont
from rbsoftskkm.dto.enums.print_line_type import PrintLineType
from rbsoftskkm.dto.positions.separator_line import SeparatorLine as _SeparatorLine
from rbsoftskkm.dto.results.picture import Picture as _Picture
from rbsoftskkm.dto.results.print_form_barcode import PrintFormBarcode


@dataclass
class PrintLine:
    """Строка печатного шаблона:

    Type - Тип строки. Используйте enum PrintLineType

    Line / LineRight - Текст (левая / правая часть)

    Alignment - Выравнивание. Используйте enum PrintAlignment

    Font - Шрифт. Используйте enum PrintFont

    Width / Scale - Ширина и масштаб

    Barcode / Picture - Штрихкод или картинка (по типу строки)
    """

    #: Тип строки. Используйте enum PrintLineType. Если не указано — Text.
    Type: PrintLineType = PrintLineType.Text

    #: Ширина. Если не указано — 0 (по содержимому).
    Width: int = 0

    #: Масштаб. Если не указано — 100%.
    Scale: int = 0

    #: Текст строки (левая часть).
    Line: Optional[str] = None

    #: Текст строки (правая часть).
    LineRight: Optional[str] = None

    #: Выравнивание. Используйте enum PrintAlignment. Если не указано — Left.
    Alignment: PrintAlignment = PrintAlignment.Left

    #: Шрифт. Используйте enum PrintFont. Если не указано — Normal.
    Font: PrintFont = PrintFont.Normal

    #: Перенос строк: false — строка обрезается; true — переносится. Если не указано — true.
    Wrap: bool = True

    #: Штрихкод.
    Barcode: Optional[PrintFormBarcode] = None

    #: Разделительная линия.
    SeparatorLine: Optional[_SeparatorLine] = None

    #: Изображение.
    Picture: Optional[_Picture] = None
