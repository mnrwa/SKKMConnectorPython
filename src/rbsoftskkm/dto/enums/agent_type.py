from __future__ import annotations

from enum import IntEnum


class AgentType(IntEnum):
    """Признак агента (тег 1222 ФФД):

    BankPaymentAgent - Банковский платежный агент

    BankPaymentSubagent - Банковский платежный субагент

    PaymentAgent - Платежный агент

    PaymentSubagent - Платёжный субагент

    Attorney - Поверенный

    Commissioner - Комиссионер

    Agent - Агент (иной тип).
    """

    #: Банковский платёжный агент.
    BankPaymentAgent = 0

    #: Банковский платёжный субагент.
    BankPaymentSubagent = 1

    #: Платёжный агент.
    PaymentAgent = 2

    #: Платёжный субагент.
    PaymentSubagent = 3

    #: Поверенный.
    Attorney = 4

    #: Комиссионер.
    Commissioner = 5

    #: Агент (иной тип).
    Agent = 6
