from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class CancelQueueTask(Sample):
    GroupPath = "Работа с ККМ|Очередь"
    Title = "Удаление задания из очереди"
    NeedDocumentId = True

    def DeleteCancelQueueTask(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.QueueTaskId = self.documentId
        kkm.CancelQueueTask()

        return kkm
