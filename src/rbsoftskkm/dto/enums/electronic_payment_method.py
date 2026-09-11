from __future__ import annotations

from enum import IntEnum


class ElectronicPaymentMethod(IntEnum):
    """Признак способа оплаты безналичными:

    FullPrepayment - Предоплата 100%

    PartialPrepayment - Предоплата

    Advance - Аванс

    FullPayment - Полный расчёт

    PartialPaymentAndCredit - Частичный расчёт и кредит

    CreditTransfer - Передача в кредит

    CreditPayment - Оплата кредита
    """

    #: Предоплата 100%.
    FullPrepayment = 0

    #: Предоплата.
    PartialPrepayment = 1

    #: Аванс.
    Advance = 2

    #: Полный расчёт.
    FullPayment = 3

    #: Частичный расчёт и кредит.
    PartialPaymentAndCredit = 4

    #: Передача в кредит.
    CreditTransfer = 5

    #: Оплата кредита.
    CreditPayment = 6
