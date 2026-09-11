from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResponseResultBase:
    """Базовый результат операции: код, описание, успех."""

    #: Код результата (0 - успех).
    Code: int = field(default=0, metadata={"json": "Code"})

    #: Описание результата или ошибки.
    Description: Optional[str] = field(default=None, metadata={"json": "Description"})

    #: Признак успешного выполнения.
    Success: bool = field(default=False, metadata={"json": "Success"})
