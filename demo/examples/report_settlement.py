from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class ReportSettlement(Sample):
    GroupPath = "Работа с ККМ|Отчеты"
    Title = "Отчёт расчётов"
    SortOrder = 0

    def PostReportSettlement(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.ReportSettlement()

        return kkm
