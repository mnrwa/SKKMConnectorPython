from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import CheckType, SkkmConnector


class GetOperationLast(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "Последняя операция"
    SortOrder = 0

    def GetGetOperationLast(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.PaymentType = CheckType.Sale
        kkm.IsProcessed = True
        kkm.GetOperationLast()

        return kkm
