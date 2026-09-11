from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.doc_position import DocPosition
from rbsoftskkm.dto.positions.fiscal_line import FiscalLine


@dataclass
class ApiPosition(DocPosition):
    """Позиция чека: фискальная строка, либо текст/штрихкод."""

    #: Фискальная строка.
    FiscalString: Optional[FiscalLine] = None
