from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Position:
    """Базовый тип позиции чека. В kkm.Positions добавляйте конкретные типы:

    FiscalLine - Фискальная (товар/услуга)

    TextLine - Текстовая

    BarcodeLine - Штрихкод

    PictureLine - Изображение

    SeparatorLine - Разделительная линия
    """

    pass
