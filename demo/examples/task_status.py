from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class TaskStatus(Sample):
    GroupPath = "Служебные"
    Title = "Статус задания"
    SortOrder = 2
    NeedDocumentId = True

    def GetTaskStatus(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.DocumentId = self.documentId
        kkm.GetTaskStatus()

        return kkm
