from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import MarkingPlannedStatus, SkkmConnector


class RequestKM(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Проверка КМ"

    def PostRequestKM(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.MarkingCode = "MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno="
        kkm.PlannedStatus = MarkingPlannedStatus.Sold
        kkm.MarkingQuantity = Decimal("1")
        kkm.WaitForResult = True
        kkm.RequestKM()

        return kkm
