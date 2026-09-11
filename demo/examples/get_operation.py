from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperation(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "Операция по id"
    NeedDocumentId = True
    SortOrder = 1

    def GetGetOperation(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DocumentId = self.documentId
        kkm.GetOperation()

        return kkm
