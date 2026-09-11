from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeleteUser(Sample):
    GroupPath = "Авторизация"
    Title = "Удаление пользователя"
    SortOrder = 3

    def DeleteDeleteUser(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.UserId = "83f43a79-027c-449e-ab97-c3f2a4b6e81c"
        kkm.DeleteUser()

        return kkm
