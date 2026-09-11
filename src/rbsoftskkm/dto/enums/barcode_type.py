from __future__ import annotations

from enum import IntEnum


class BarcodeType(IntEnum):
    """Тип штрихкода для печати в документе.

    QR - QR-код

    EAN13 - EAN-13

    EAN8 - EAN-8

    EAN13 - EAN-13

    CODE39 - Code 39

    CODE93 - Code 93

    CODE128 - Code 128

    UPCA - UPC-A

    UPCE - UPC-E

    ITF - Interleaved 2 of 5

    CODABAR - Codabar

    PDF417 - PDF417

    CODE32 - Code 32
    """

    #: QR-код
    QR = 0

    #: EAN-13
    EAN13 = 1

    #: EAN-8
    EAN8 = 2

    #: Code 39
    CODE39 = 3

    #: Code 93
    CODE93 = 4

    #: Code 128
    CODE128 = 5

    #: UPC-A
    UPCA = 6

    #: UPC-E
    UPCE = 7

    #: Interleaved 2 of 5
    ITF = 8

    #: Codabar
    CODABAR = 9

    #: PDF417
    PDF417 = 10

    #: Code 32
    CODE32 = 11
