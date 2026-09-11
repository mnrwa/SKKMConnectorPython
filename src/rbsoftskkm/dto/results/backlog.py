from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Backlog:
    """Данные о непереданных документах"""

    #: Количество непереданных документов.
    DocumentsCounter: int = 0

    #: Номер первого непереданного документа.
    DocumentFirstNumber: int = 0

    #: Дата и время первого из непереданных документов.
    DocumentFirstDateTime: datetime = datetime.min
