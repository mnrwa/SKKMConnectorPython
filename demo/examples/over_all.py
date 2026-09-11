from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class OverAll(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Общие счётчики"
    SortOrder = 13

    def GetOverAll(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetOverAll()

        return kkm
