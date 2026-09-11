from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class ShiftList(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Список закрытий смен"
    SortOrder = 7

    def GetShiftList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetShiftList()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
