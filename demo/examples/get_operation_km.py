from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperationKm(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "Коды маркировки операции"
    NeedDocumentId = True
    SortOrder = 4

    def GetGetOperationKm(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DocumentId = self.documentId
        kkm.GetOperationKm()

        return kkm
