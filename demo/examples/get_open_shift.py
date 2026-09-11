from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetOpenShift(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Результат открытия смены"
    NeedDocumentId = True
    SortOrder = 1

    def GetOpenShiftById(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetOpenShift()

        return kkm
