from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class ReportX(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "X-отчёт"
    SortOrder = 8

    def PostReportX(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.ReportX()

        return kkm
