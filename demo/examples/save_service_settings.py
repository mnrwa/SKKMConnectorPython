from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import ProxyConfig, ServiceSettings, SkkmConnector


class SaveServiceSettings(Sample):
    GroupPath = "Администрирование|Служба"
    Title = "Сохранение настроек службы"
    SortOrder = 1

    def PostSaveServiceSettings(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.ServiceSettings = ServiceSettings(
            WcfServicePort=4398,
            WebServicePort=8888,
            ServiceTimeOut="00:00:15",
            ProxyServerSettings=ProxyConfig(IsUseProxy=False, IpAddress="", Port=0, Name="", Password=""),
            MaxQueueSize=100,
            RepeatPrintingOnError=False,
        )

        kkm.SaveServiceSettings()

        return kkm
