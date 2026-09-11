from __future__ import annotations

from enum import IntEnum


class KmConfirmationType(IntEnum):
    """Признак подтверждения кода маркировки при закрытии сессии регистрации:

    Included - Код маркировки включён в документ реализации

    NotIncluded - Код маркировки не включён в документ реализации
    """

    #: Код маркировки включён в документ реализации.
    Included = 0

    #: Код маркировки не включён в документ реализации.
    NotIncluded = 1
