from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Connect(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Информация о ККТ"
    SortOrder = 2

    def GetConnect(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Connect()

        return kkm
