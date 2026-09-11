from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.results.doc_data import DocData


@dataclass
class ShiftCounters:
    """Счетчики фискальных операций за кассовую смену"""

    #: Общая сумма коррекций за смену.
    SumCorrection: Decimal = Decimal("0")

    #: Количество коррекций за смену.
    NumberCorrections: int = 0

    #: Приход
    Sales: Optional[DocData] = None

    #: Возврат прихода
    SalesReturn: Optional[DocData] = None

    #: Коррекция прихода
    SalesCorrection: Optional[DocData] = None

    #: Коррекция возврата прихода
    SalesReturnCorrection: Optional[DocData] = None

    #: Расход
    Purchases: Optional[DocData] = None

    #: Возврат расхода
    PurchasesReturn: Optional[DocData] = None

    #: Коррекция расхода
    PurchasesCorrection: Optional[DocData] = None

    #: Коррекция возврата расхода
    PurchasesReturnCorrection: Optional[DocData] = None
