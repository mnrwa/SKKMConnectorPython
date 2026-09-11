from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.results.doc_data_payments import DocDataPayments
from rbsoftskkm.dto.results.reg_data import RegData


@dataclass
class DocData:
    """Счетчик документов"""

    #: Количество документов
    Count: int = 0

    #: Сумма по документам
    Sum: Decimal = Decimal("0")

    #: Разбивка суммы по видам оплаты
    Payments: Optional[DocDataPayments] = None

    #: Скидки: количество и сумма.
    Discount: Optional[RegData] = None

    #: Надбавки (наценки): количество и сумма.
    Adding: Optional[RegData] = None
