from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from rbsoftskkm.dto.positions.position import Position


@dataclass
class BarcodeLine(Position):
    """Строка штрихкода в чеке:

    Type - Тип штрихкода

    Value - Значение
    """

    #: Тип штрихкода
    Type: str = ""

    #: Значение штрихкода
    Barcode: str = field(default="", metadata={"json": "Value"})

    #: Значение штрихкода в Base64
    ValueBase64: Optional[str] = None

    #: Выравнивание штрихкода
    Alignment: Optional[str] = None
