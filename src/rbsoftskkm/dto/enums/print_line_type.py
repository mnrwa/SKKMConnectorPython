from __future__ import annotations

from enum import IntEnum


class PrintLineType(IntEnum):
    """Тип строки печатного шаблона / печатной формы:

    Fiscal - Фискальная

    Text - Текстовая

    Barcode - Штрихкод

    Picture - Изображение

    Separator - Разделительная линия
    """

    #: Фискальная строка.
    Fiscal = 0

    #: Текстовая строка.
    Text = 1

    #: Штрихкод.
    Barcode = 2

    #: Изображение.
    Picture = 3

    #: Разделительная линия.
    Separator = 4
