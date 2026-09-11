from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import DeviceSettings, SkkmConnector


class SetDeviceFont(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Настройки шрифта шаблона"
    SortOrder = 11

    def PostSetDeviceFont(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName

        kkm.DeviceSettings = DeviceSettings(
            TemplateSettingH1="1",
            TemplateSettingH2="1",
            TemplateSettingH3="2",
            TemplateSettingH4="2",
            TemplateSettingH5="2",
        )

        kkm.SetDeviceFont()

        return kkm
