from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class CheckItem:
    """Позиция сохранённого чека"""

    #: Название.
    Name: Optional[str] = None

    #: Количество товара.
    Quantity: Decimal = Decimal("0")

    #: Цена позиции.
    Price: Decimal = Decimal("0")

    #: Сумма с учётом скидки.
    Sum: Decimal = Decimal("0")

    #: Отдел.
    Department: Optional[int] = None

    #: Фискальный режим.
    IsFiscal: bool = False

    #: Ставка НДС.
    TaxValue: int = 0

    #: Сумма НДС.
    TaxSum: Decimal = Decimal("0")

    #: Признак способа расчёта
    PaymentMode: int = 0

    #: Признак предмета расчёта (тег 1030 / 1212).
    ItemType: int = 0

    #: Сумма акциза с учётом копеек, включённая в стоимость предмета расчёта.
    ExciseAmount: Optional[Decimal] = None

    #: Мера количества предмета расчёта.
    MeasureOfQuantity: Optional[int] = None

    #: Скидка (>0) или наценка (<0).
    DiscountInfoValue: Decimal = Decimal("0")

    #: Дополнительный реквизит предмета расчёта.
    AdditionalAttribute: Optional[str] = None
