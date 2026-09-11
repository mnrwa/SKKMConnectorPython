from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckCorrection105(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.0.5"
    Title = "Получение чека коррекции 1.0.5"
    NeedDocumentId = True

    def GetCheckCorrection105ById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetCorrection105()

        return kkm
