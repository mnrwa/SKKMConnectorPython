from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class Check(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Чек по id"
    NeedDocumentId = True
    SortOrder = 4

    def GetCheck(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetCheck()

        return kkm
