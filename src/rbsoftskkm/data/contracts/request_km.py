from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class RequestKm:
    """Параметры проверяемого кода маркировки."""

    #: Идентификатор запроса проверки.
    Guid: Optional[str] = None

    #: Не отправлять запрос на сервер ОИСМ (только локальная проверка).
    NotSendToServer: bool = False

    #: Ждать ответ ОИСМ.
    WaitForResult: bool = False

    #: Код маркировки в Base64.
    MarkingCode: Optional[str] = None

    #: Планируемый статус товара (тег 2003).
    PlannedStatus: int = 0

    #: Количество предмета расчёта.
    Quantity: Decimal = Decimal("0")

    #: Мера количества предмета расчёта (таблица 114 ФФД).
    MeasureOfQuantity: int = 0

    #: Числитель дробного количества маркированного товара.
    FractionalQuantityNumerator: Optional[int] = None

    #: Знаменатель дробного количества маркированного товара.
    FractionalQuantityDenominator: Optional[int] = None
