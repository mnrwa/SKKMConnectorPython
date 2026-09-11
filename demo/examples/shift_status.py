from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class ShiftStatus(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Статус смены"
    SortOrder = 8

    def GetShiftStatus(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetShiftStatus()

        return kkm
