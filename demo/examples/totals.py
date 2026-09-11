from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Totals(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Итоги смены"
    SortOrder = 9

    def GetTotals(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetTotals()

        return kkm
