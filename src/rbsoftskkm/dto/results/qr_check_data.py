from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class QrCheckData:
    """Данные для отображения QR-кода чека (QrCheckData)."""

    #: Дата создания документа.
    Date: datetime = datetime.min

    #: Сумма чека.
    Amount: Decimal = Decimal("0")

    #: Фискальный накопитель.
    Fn: Optional[str] = None

    #: Фискальный документ.
    Fd: int = 0

    #: Фискальный признак.
    Fp: Optional[str] = None

    #: Тип операции: 1 — приход; 2 — возврат прихода; 4 — расход; 5 — возврат расхода; 7 — коррекция прихода; 9 — коррекция расхода.
    N: int = 0
