from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetReportSettlementList(Sample):
    GroupPath = "Работа с ККМ|Отчеты"
    Title = "Список отчётов расчётов"
    SortOrder = 3

    def GetReportSettlementListByPeriod(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetReportSettlementList()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
