from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ProcessingKmResult:
    """Результат проверки кода маркировки в ОИСМ"""

    #: Идентификатор запроса КМ
    Guid: Optional[str] = None

    #: Итог проверки кода маркировки.
    Result: bool = False

    #: Код результата проверки (тег 2106 ФФД).
    ResultCode: int = 0

    #: Статус информации о коде маркировки (тег 2109 ФФД).
    StatusInfo: Optional[int] = None

    #: Код обработки запроса (тег 2105 ФФД).
    HandleCode: int = 0

    #: Статус получения результата от ОИСМ: 0 — получен; 1 — ещё не получен; 2 — не может быть получен.
    RequestStatus: int = 0
