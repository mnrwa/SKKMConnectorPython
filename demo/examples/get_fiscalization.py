from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetFiscalization(Sample):
    GroupPath = "Работа с ККМ|Фискализация"
    Title = "Результат фискализации"
    NeedDocumentId = True
    SortOrder = 2

    def GetGetFiscalization(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetFiscalization()

        return kkm
