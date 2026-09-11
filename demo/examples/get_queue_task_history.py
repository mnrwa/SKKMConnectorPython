from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetQueueTaskHistory(Sample):
    GroupPath = "Работа с ККМ|Очередь"
    Title = "История обработки задания"
    NeedDocumentId = True

    def GetGetQueueTaskHistory(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.QueueTaskId = self.documentId
        kkm.GetQueueTaskHistory()

        return kkm
