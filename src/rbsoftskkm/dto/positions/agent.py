from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Agent:
    """Данные агента в чеке:

    PayingAgentOperation - Операция платёжного агента

    PayingAgentPhone - Телефон(ы) платёжного агента

    ReceivePaymentsOperatorPhone - Телефон(ы) оператора по приёму платежей

    MoneyTransferOperatorPhone - Телефон(ы) оператора перевода

    MoneyTransferOperatorName - Наименование оператора перевода

    MoneyTransferOperatorAddress - Адрес оператора перевода

    MoneyTransferOperatorVatin - ИНН оператора перевода
    """

    #: Операция платёжного агента.
    PayingAgentOperation: Optional[str] = None

    #: Телефон платёжного агента.
    PayingAgentPhone: Optional[list[str]] = None

    #: Телефон оператора по приёму платежей.
    ReceivePaymentsOperatorPhone: Optional[list[str]] = None

    #: Телефон оператора перевода.
    MoneyTransferOperatorPhone: Optional[list[str]] = None

    #: Наименование оператора перевода.
    MoneyTransferOperatorName: Optional[str] = None

    #: Адрес оператора перевода.
    MoneyTransferOperatorAddress: Optional[str] = None

    #: ИНН оператора перевода.
    MoneyTransferOperatorVatin: Optional[str] = None
