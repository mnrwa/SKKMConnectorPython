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
class PrintFormLine:
    """Строка печатной формы."""

    #: Тип строки. Если не указано — Text.
    Type: PrintLineType = PrintLineType.Fiscal

    #: Текст строки (левая часть).
    Line: Optional[str] = None

    #: Текст строки (правая часть).
    LineRight: Optional[str] = None

    #: Выравнивание. Если не указано — Left.
    Alignment: PrintAlignment = PrintAlignment.Left

    #: Шрифт. Если не указано — Normal.
    Font: PrintFont = PrintFont.Normal

    #: Признак, что шрифт задан явно во входящих данных или при создании строки.
    IsFontSpecified: bool = False

    #: Ширина. Если не указано — 0 (по содержимому).
    Width: int = 0

    #: Масштаб. Если не указано — 100%.
    Scale: int = 0

    #: Признак переноса строк: false — строка обрезается; true — переносится. Если не указано — true.
    Wrap: bool = False

    #: Разделительная линия.
    SeparatorLine: Optional[_SeparatorLine] = None

    #: Изображение.
    Picture: Optional[_Picture] = None

    #: Штрихкод.
    Barcode: Optional[PrintFormBarcode] = None

    #: Строки, выводимые справа или слева от штрихкода.
    BarcodeLines: Optional[list[str]] = None

    #: Признак создания строки из печатного шаблона.
    IsCreateFromTemplate: bool = False
