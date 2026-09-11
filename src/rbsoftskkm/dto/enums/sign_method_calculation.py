from __future__ import annotations

from enum import IntEnum


class SignMethodCalculation(IntEnum):
    """Признак способа расчёта (тег 1214 ФФД):

    NotApplicable - Не применяется

    FullPrepayment - Предоплата полная

    PartialPrepayment - Предоплата частичная

    Advance - Аванс

    FullPayment - Полная оплата

    PartialPaymentAndCredit - Частичная оплата и кредит

    CreditTransfer - Передача в кредит

    CreditPayment - Оплата кредита
    """

    #: Не применяется.
    NotApplicable = 0

    #: Предоплата полная.
    FullPrepayment = 1

    #: Предоплата частичная.
    PartialPrepayment = 2

    #: Аванс.
    Advance = 3

    #: Полная оплата.
    FullPayment = 4

    #: Частичная оплата и кредит.
    PartialPaymentAndCredit = 5

    #: Передача в кредит.
    CreditTransfer = 6

    #: Оплата кредита.
    CreditPayment = 7
