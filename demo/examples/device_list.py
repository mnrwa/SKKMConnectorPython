from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeviceList(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Список ККМ"
    SortOrder = 0

    def GetDeviceList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetDeviceList()

        return kkm
