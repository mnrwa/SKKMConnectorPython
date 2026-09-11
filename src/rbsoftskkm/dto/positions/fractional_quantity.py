from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FractionalQuantity:
    """Дробное количество предмета расчёта:

    Numerator - Числитель

    Denominator - Знаменатель

    Используется вместе с мерой количества при частичной реализации маркированного товара.
    """

    #: Числитель.
    Numerator: int = 0

    #: Знаменатель.
    Denominator: int = 0
