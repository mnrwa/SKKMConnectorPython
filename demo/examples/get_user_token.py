from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetUserToken(Sample):
    GroupPath = "Авторизация"
    Title = "Получение токена"
    SortOrder = 0

    def GetGetUserToken(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.AuthUserName = "Admin"
        kkm.AuthPassword = "Admin"
        kkm.GetUserToken()

        return kkm
