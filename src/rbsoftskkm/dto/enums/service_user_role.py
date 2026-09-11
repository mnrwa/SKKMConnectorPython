from __future__ import annotations

from enum import IntEnum


class ServiceUserRole(IntEnum):
    """Роль пользователя сервера ККМ:

    Administrator - Администратор

    Employee - Сотрудник
    """

    #: Администратор.
    Administrator = 0

    #: Сотрудник.
    Employee = 1
