from __future__ import annotations

from dataclasses import dataclass, field

from rbsoftskkm.dto.marking.code_mark_info import CodeMarkInfo


@dataclass
class MarkingVerifyResult:
    """Результат проверки кода маркировки."""

    #: Код результата проверки.
    Code: int = 0

    #: Описание результата проверки.
    Description: str = ""

    #: Данные проверки кодов маркировки.
    Codes: list[CodeMarkInfo] = field(default_factory=list)

    #: Идентификатор операции проверки.
    ReqId: str = ""

    #: Временная метка операции проверки.
    ReqTimestamp: int = 0

    #: Признак офлайн-проверки.
    IsCheckedOffline: bool = False
