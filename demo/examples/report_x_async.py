from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class ReportXAsync(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Асинхронное получение X-отчёта"
    SortOrder = 9

    def PostReportXAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.ReportXAsync()

        return kkm
