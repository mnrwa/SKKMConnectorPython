from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class ReportSettlementAsync(Sample):
    GroupPath = "Работа с ККМ|Отчеты"
    Title = "Асинхронный отчёт о расчётах"
    SortOrder = 1

    def PostReportSettlementAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.ReportSettlementAsync()

        return kkm
