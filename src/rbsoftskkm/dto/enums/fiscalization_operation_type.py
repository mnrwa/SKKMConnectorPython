from __future__ import annotations

from enum import IntEnum


class FiscalizationOperationType(IntEnum):
    """Тип операции фискализации:

    Registration - Регистрация

    ChangeParameters - Изменение параметров

    CloseFn - Закрытие ФН
    """

    #: Регистрация.
    Registration = 1

    #: Изменение параметров.
    ChangeParameters = 2

    #: Закрытие ФН.
    CloseFn = 3
