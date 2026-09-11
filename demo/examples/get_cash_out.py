from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCashOut(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Выемка по id"
    NeedDocumentId = True
    SortOrder = 8

    def GetCashOutById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetCashOut()

        return kkm
