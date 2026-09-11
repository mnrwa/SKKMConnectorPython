from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperationRelated(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "Связанные операции"
    NeedDocumentId = True
    SortOrder = 5

    def GetGetOperationRelated(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DocumentId = self.documentId
        kkm.GetOperationRelated()

        return kkm
