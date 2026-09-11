from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeleteDevice(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Удаление ККТ"
    SortOrder = 4

    def DeleteDeleteDevice(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DeleteDevice()

        return kkm
