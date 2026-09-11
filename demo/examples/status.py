from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Status(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Статус ККМ"
    SortOrder = 7

    def GetStatus(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetStatus()

        return kkm
