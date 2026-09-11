from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckList(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Список чеков за период"
    SortOrder = 5

    def GetGetCheckList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetCheckList()

        return kkm
