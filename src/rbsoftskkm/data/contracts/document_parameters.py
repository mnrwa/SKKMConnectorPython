from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.data.contracts.doc_position import DocPosition


@dataclass
class DocumentParameters(CheckbaseParameters):
    """Тело запроса печати нефискального документа."""

    #: Строки документа
    Positions: Optional[list[DocPosition]] = None
