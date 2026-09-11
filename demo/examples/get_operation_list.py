from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOperationList(Sample):
    GroupPath = "Работа с ККМ|Операции"
    Title = "Список операций"
    SortOrder = 6

    def GetGetOperationList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.ShiftsFrom = self.fromDate
        kkm.ShiftsTo = self.toDate
        kkm.GetOperationList()

        return kkm
