from __future__ import annotations

from enum import IntEnum


class MeasureOfQuantity(IntEnum):
    """Мера количества предмета расчёта (таблица 114 ФФД):

    Piece - Штука или единица (поштучная реализация)

    Gram - Грамм

    Kilogram - Килограмм

    Tonne - Тонна

    Centimeter - Сантиметр

    Decimeter - Дециметр

    Meter - Метр

    SquareCentimeter - Квадратный сантиметр

    SquareDecimeter - Квадратный дециметр

    SquareMeter - Квадратный метр

    Milliliter - Миллилитр

    Liter - Литр

    CubicMeter - Кубический метр

    KilowattHour - Киловатт-час

    Gigacalorie - Гигакалория

    Day - Сутки

    Hour - Час

    Minute - Минута

    Second - Секунда

    Kilobyte - Килобайт

    Megabyte - Мегабайт

    Gigabyte - Гигабайт

    Terabyte - Терабайт

    Other - Иная единица измерения
    """

    #: Штука или единица (поштучная реализация).
    Piece = 0

    #: Грамм.
    Gram = 10

    #: Килограмм.
    Kilogram = 11

    #: Тонна.
    Tonne = 12

    #: Сантиметр.
    Centimeter = 20

    #: Дециметр.
    Decimeter = 21

    #: Метр.
    Meter = 22

    #: Квадратный сантиметр.
    SquareCentimeter = 30

    #: Квадратный дециметр.
    SquareDecimeter = 31

    #: Квадратный метр.
    SquareMeter = 32

    #: Миллилитр.
    Milliliter = 40

    #: Литр.
    Liter = 41

    #: Кубический метр.
    CubicMeter = 42

    #: Киловатт-час.
    KilowattHour = 50

    #: Гигакалория.
    Gigacalorie = 51

    #: Сутки.
    Day = 70

    #: Час.
    Hour = 71

    #: Минута.
    Minute = 72

    #: Секунда.
    Second = 73

    #: Килобайт.
    Kilobyte = 80

    #: Мегабайт.
    Megabyte = 81

    #: Гигабайт.
    Gigabyte = 82

    #: Терабайт.
    Terabyte = 83

    #: Иная единица измерения.
    Other = 255
