from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.service_user_role import ServiceUserRole


@dataclass
class ServiceUser:
    """Пользователь сервера ККМ:

    Id - Идентификатор пользователя на сервере (нужен при изменении / удалении)

    UserName - Логин для входа

    FullName - Отображаемое ФИО / полное имя

    Vatin - ИНН пользователя

    Role - Роль. Используйте enum ServiceUserRole

    TokenId - Идентификатор токена API (обычно приходит в ответе сервера)

    Password - Пароль (указывайте при создании пользователя и смене пароля)
    """

    #: Идентификатор пользователя на сервере ККМ. Нужен при изменении и удалении.
    Id: Optional[str] = None

    #: Логин для входа (Basic Auth / учётная запись сервера).
    UserName: str = ""

    #: Полное имя пользователя (ФИО или отображаемое имя).
    FullName: str = ""

    #: ИНН пользователя (при наличии).
    Vatin: str = ""

    #: Роль пользователя. Используйте enum ServiceUserRole.
    Role: ServiceUserRole = ServiceUserRole.Administrator

    #: Идентификатор токена API. Обычно заполняется сервером в ответе.
    TokenId: Optional[str] = None

    #: Пароль учётной записи. Указывайте при создании пользователя и при смене пароля.
    Password: Optional[str] = None
