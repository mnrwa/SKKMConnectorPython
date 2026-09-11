from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetReportXList(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Список X-отчётов"
    SortOrder = 11

    def GetReportXListByPeriod(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetReportXList()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
