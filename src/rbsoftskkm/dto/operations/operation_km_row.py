from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class OperationKmRow:
    """Строка журнала кодов маркировки операции."""

    #: Код маркировки (КиЗ).
    Cis: str = ""

    #: Время проверки кода.
    CheckedAt: datetime = datetime.min

    #: Код маркировки без крипто-подписи.
    PrintView: str = ""

    #: Сообщение о результате проверки.
    Message: str = ""

    #: Статус проверки кода.
    CheckStatus: int = 0

    #: Наименование позиции чека.
    PositionName: str = ""

    #: Идентификаторы связанных документов.
    DocIds: list[str] = field(default_factory=list)

    #: Цена продажи (в копейках).
    SalePrice: int = 0

    #: Имя устройства.
    DeviceName: str = ""

    #: Идентификатор марки.
    MarkId: str = ""

    #: Метод проверки кода маркировки.
    KmVerificationMethod: int = 0

    #: Инициатор проверки кода маркировки.
    KmCheckInitiator: int = 0
