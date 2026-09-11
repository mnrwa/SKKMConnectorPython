from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetFiscalSign(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Фискальный признак"
    SortOrder = 6

    def GetFiscalSignByDocNumber(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.CheckNumber = 1
        kkm.GetFiscalSign()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
