from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckCorrection120(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.2"
    Title = "Получение чека коррекции 1.2"
    NeedDocumentId = True

    def GetCheckCorrection120ById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetCorrection120()

        return kkm
