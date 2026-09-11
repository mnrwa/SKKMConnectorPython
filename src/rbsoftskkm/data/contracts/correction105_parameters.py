from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.dto.correction_data import CorrectionData as _CorrectionData
from rbsoftskkm.dto.payments import Payments as _Payments


@dataclass
class Correction105Parameters(CheckbaseParameters):
    """Тело запроса печати чека коррекции ФФД 1.05."""

    #: Тип чека
    PaymentType: int = 0

    #: Код системы налогообложения.
    TaxVariant: int = 0

    #: Дополнительный реквизит чека (БСО), тег 1192
    AdditionalAttribute: Optional[str] = None

    #: Данные коррекции.
    CorrectionData: Optional[_CorrectionData] = None

    #: Список оплаты
    Payments: Optional[_Payments] = None

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
