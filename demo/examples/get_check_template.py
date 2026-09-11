from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckTemplate(Sample):
    GroupPath = "Работа с ККМ|Шаблоны чека"
    Title = "Получение шаблона чека"

    def GetGetCheckTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.TemplateName = "piot_test_classic_5.1"
        kkm.GetCheckTemplate()

        return kkm
