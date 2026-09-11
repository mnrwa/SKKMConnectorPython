from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Ping(Sample):
    GroupPath = "Служебные"
    Title = "Проверка доступности сервера"
    SortOrder = 0

    def GetPing(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.Ping()

        return kkm
