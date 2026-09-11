from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from rbsoftskkm.dto.cashier import Cashier as _Cashier


@dataclass
class CheckbaseParameters:
    """Базовые параметры кассового документа"""

    #: Имя кассы
    DeviceName: Optional[str] = field(default=None, metadata={"order": -3})

    #: Идентификатор документа
    DocId: Optional[str] = field(default=None, metadata={"order": -2})

    #: Кассир
    Cashier: Optional[_Cashier] = field(default=None, metadata={"order": -1})
