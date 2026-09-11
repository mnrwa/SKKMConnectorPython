from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Correction105Taxes:
    """Суммы НДС по ставкам для чека коррекции ФФД 1.05:

    SumTax0 / SumTax5 / SumTax7 / SumTax10 / SumTax18 / SumTax20 / SumTax22 - Суммы по ставкам

    SumTaxNone - Без НДС

    SumTax105 / SumTax107 / SumTax110 / SumTax118 / SumTax120 / SumTax122 - Расчётные ставки

    Укажите только те ставки, которые относятся к корректируемому расчёту.
    """

    #: Сумма расчёта по ставке НДС 0%.
    SumTax0: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 5%.
    SumTax5: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 7%.
    SumTax7: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 10%.
    SumTax10: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 18%.
    SumTax18: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 20%.
    SumTax20: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 22%.
    SumTax22: Optional[Decimal] = None

    #: Сумма расчёта без НДС.
    SumTaxNone: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 5/105.
    SumTax105: Optional[Decimal] = None

    #: Сумма НДС чека по ставке 7/107.
    SumTax107: Optional[Decimal] = None

    #: Сумма НДС чека по расч. ставке 10/110.
    SumTax110: Optional[Decimal] = None

    #: Сумма НДС чека по расч. ставке 18/118.
    SumTax118: Optional[Decimal] = None

    #: Сумма НДС чека по расч. ставке 20/120.
    SumTax120: Optional[Decimal] = None

    #: Сумма НДС чека по расч. ставке 22/122.
    SumTax122: Optional[Decimal] = None
