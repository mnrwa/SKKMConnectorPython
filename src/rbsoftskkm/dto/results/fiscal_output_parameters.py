from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.results.backlog import Backlog as _Backlog
from rbsoftskkm.dto.results.warnings import Warnings


@dataclass
class FiscalOutputParameters:
    """Вложенный блок OutputParameters в ответе сервера."""

    #: Номер чека за смену.
    NumberOfChecks: int = 0

    #: Дата и время ККТ.
    DateTime: Optional[str] = None

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер фискального документа / чека.
    CheckNumber: int = 0

    #: Остаток наличных в ящике.
    CashBalance: Decimal = Decimal("0")

    #: Срок действия ФН.
    FnValidityDate: Optional[str] = None

    #: Очередь непереданных документов.
    Backlog: Optional[_Backlog] = None

    #: Предупреждения ФН.
    FnWarnings: Optional[Warnings] = None

    #: Остаток ресурса ФН в днях.
    ResourcesFn: int = 0
