from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperationHistory(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "История операции"
    NeedDocumentId = True
    SortOrder = 2

    def GetGetOperationHistory(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DocumentId = self.documentId
        kkm.GetOperationHistory()

        return kkm
