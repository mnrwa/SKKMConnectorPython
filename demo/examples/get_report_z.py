from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetReportZ(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Результат закрытия смены"
    NeedDocumentId = True
    SortOrder = 6

    def GetGetReportZ(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetReportZ()

        return kkm
