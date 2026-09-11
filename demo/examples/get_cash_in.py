from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCashIn(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Внесение по id"
    NeedDocumentId = True
    SortOrder = 5

    def GetCashInById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetCashIn()

        return kkm
