from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetSlip(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки"
    Title = "Получение нефискального документа"
    NeedDocumentId = True
    SortOrder = 3

    def GetGetSlip(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetSlip()

        return kkm
