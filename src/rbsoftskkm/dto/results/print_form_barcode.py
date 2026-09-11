from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.barcode_print_text import BarcodePrintText
from rbsoftskkm.dto.enums.barcode_type import BarcodeType


@dataclass
class PrintFormBarcode:
    """Штрихкод в печатной форме."""

    #: Тип штрихкода.
    Type: Optional[BarcodeType] = None

    #: Значение штрихкода.
    Value: Optional[str] = None

    #: Изображение штрихкода, закодированное в Base64.
    PictureBase64: Optional[str] = None

    #: Способ печати текста штрихкода (только для одномерных).
    PrintText: BarcodePrintText = BarcodePrintText.None_

    #: Высота штрихкода в точках. Допустимые значения: 0..1199.
    Height: int = 0

    #: Ширина штриха в точках. Допустимые значения: 0..1199. Рекомендуемое значение — 2.
    BarWidth: int = 0
