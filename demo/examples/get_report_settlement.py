from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetReportSettlement(Sample):
    GroupPath = "Работа с ККМ|Отчеты"
    Title = "Отчёт расчётов по id"
    NeedDocumentId = True
    SortOrder = 2

    def GetReportSettlementById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetReportSettlement()

        return kkm
