from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetQueueTask(Sample):
    GroupPath = "Работа с ККМ|Очередь"
    Title = "Актуальный статус задачи"
    NeedDocumentId = True

    def GetGetQueueTask(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.QueueTaskId = self.documentId
        kkm.GetQueueTask()

        return kkm
