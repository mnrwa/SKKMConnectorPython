from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetReportX(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Результат X-отчёта"
    NeedDocumentId = True
    SortOrder = 10

    def GetGetReportX(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetReportX()

        return kkm
