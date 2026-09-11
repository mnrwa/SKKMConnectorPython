from __future__ import annotations

from enum import IntEnum


class PrintFont(IntEnum):
    """Шрифт текстовой строки документа:

    Normal - Обычный

    Bold - Жирный

    Small - Мелкий

    Medium - Средний

    Big - Крупный

    H1 - Заголовок 1

    H2 - Заголовок 2

    H3 - Заголовок 3

    H4 - Заголовок 4

    H5 - Заголовок 5
    """

    #: Обычный
    Normal = 0

    #: Жирный
    Bold = 1

    #: Мелкий
    Small = 2

    #: Средний
    Medium = 3

    #: Крупный
    Big = 4

    #: Заголовок 1
    H1 = 5

    #: Заголовок 2
    H2 = 6

    #: Заголовок 3
    H3 = 7

    #: Заголовок 4
    H4 = 8

    #: Заголовок 5
    H5 = 9
