from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetVersion(Sample):
    GroupPath = "Служебные"
    Title = "Текущая версия сервера"
    SortOrder = 1

    def GetGetVersion(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetVersion()

        return kkm
