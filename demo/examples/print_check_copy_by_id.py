from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class PrintCheckCopyById(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Копия чека по идентификатору"
    NeedDocumentId = True
    SortOrder = 3

    def PostPrintCheckCopyById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.PrintCheckCopy()

        return kkm
