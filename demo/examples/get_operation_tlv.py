from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperationTlv(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "TLV операции"
    NeedDocumentId = True
    SortOrder = 3

    def GetGetOperationTlv(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DocumentId = self.documentId
        kkm.GetOperationTlv()

        return kkm
