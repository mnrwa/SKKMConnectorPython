from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RequestKmResult:
    """Результат локальной проверки кода маркировки"""

    #: Признак наличия связи с ОИСМ на момент отправки запроса.
    IsmConnected: bool = field(default=False, metadata={"json": "ISMConnected"})

    #: Признак того, что проверка формата кода маркировки прошла успешно.
    FormatChecking: bool = False

    #: Признак того, что проверка кода маркировки поставлена в обработку.
    Checking: bool = False

    #: Результат проверки, если он уже доступен на момент ответа.
    CheckingResult: bool = False

    #: Штрихкод после приведения к виду со спецсимволами GS.
    Barcode: Optional[str] = None
