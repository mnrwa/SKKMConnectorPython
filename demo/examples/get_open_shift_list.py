from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOpenShiftList(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Список открытий смен"
    SortOrder = 2

    def GetOpenShiftListByPeriod(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetOpenShiftList()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
