from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class PrintForm(Sample):
    GroupPath = "Служебные"
    Title = "Печатная форма чека"
    SortOrder = 3
    NeedDocumentId = True

    def GetPrintForm(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetPrintForm()

        return kkm
