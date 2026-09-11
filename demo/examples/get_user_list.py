from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetUserList(Sample):
    GroupPath = "Авторизация"
    Title = "Список пользователей"
    SortOrder = 1

    def GetGetUserList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetUserList()

        return kkm
