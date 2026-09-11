from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import ServiceUser, ServiceUserRole, SkkmConnector


class UpdateUser(Sample):
    GroupPath = "Авторизация"
    Title = "Редактирование пользователя"
    SortOrder = 4

    def PutUpdateUser(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.UserId = "83f43a79-027c-449e-ab97-c3f2a4b6e81c"

        kkm.ServiceUser = ServiceUser(
            UserName="artyom",
            Password="Admin21",
            FullName="Челпанов Артем",
            Vatin="221431",
            Role=ServiceUserRole.Employee,
        )

        kkm.UpdateUser()

        return kkm
