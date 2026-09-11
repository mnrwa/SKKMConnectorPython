from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import ServiceUser, ServiceUserRole, SkkmConnector


class AddUser(Sample):
    GroupPath = "Авторизация"
    Title = "Добавление пользователя"
    SortOrder = 2

    def PostAddUser(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.ServiceUser = ServiceUser(
            UserName="Alex",
            FullName="Алексей Петров",
            Password="Admin",
            Vatin="222222",
            Role=ServiceUserRole.Employee,
        )

        kkm.AddUser()

        return kkm
