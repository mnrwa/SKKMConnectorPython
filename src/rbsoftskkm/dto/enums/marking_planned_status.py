from __future__ import annotations

from enum import IntEnum


class MarkingPlannedStatus(IntEnum):
    """Планируемый статус товара при проверке кода маркировки (таблица 105 ФФД):

    NotSpecified - Не задан (значение по умолчанию в запросе)

    Sold - Реализован

    InSale - Мерный товар в стадии реализации

    Returned - Возвращён

    PartiallyReturned - Часть товара возвращена

    Unchanged - Статус не изменился
    """

    #: Не задан (значение по умолчанию в запросе).
    NotSpecified = 0

    #: Реализован.
    Sold = 1

    #: Мерный товар в стадии реализации.
    InSale = 2

    #: Возвращён.
    Returned = 3

    #: Часть товара возвращена.
    PartiallyReturned = 4

    #: Статус не изменился.
    Unchanged = 255
