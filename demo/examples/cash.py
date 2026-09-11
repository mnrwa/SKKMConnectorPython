from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Cash(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Остаток в ящике"
    SortOrder = 1

    def GetCash(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetCash()

        return kkm
