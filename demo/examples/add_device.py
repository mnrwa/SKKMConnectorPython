from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import ConnectionMethod, DeviceSettings, DeviceType, SkkmConnector


class AddDevice(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Добавление ККТ"
    SortOrder = 3

    def PostAddDevice(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName

        kkm.DeviceSettings = DeviceSettings(
            DeviceName=self.deviceName,
            DeviceType=DeviceType.Shtrih,
            Available=True,
            MethodConnection=ConnectionMethod.Com,
            PortNumber=1,
            BaudRate=9600,
            IpAddress="192.168.0.109",
            TcpPort=7778,
            Password="30",
            SerialNumber="0392790042005043",
            SenderEmail="ivanov@mail.ru",
            Cashier=self.cashierName,
            CashierVatin=self.cashierVatin,
            Vatin="7700000000",
            OrganizationName="ООО 'Ромашка'",
            SaleAddress="г.Улан-Удэ, ул.Виноградная, д11А, офис 25",
            ClientSaleLocation="Офис",
            TimeoutConnection=5000,
            TimeoutWaitForPrinting=60000,
            OfdAddress="ofd.example.ru",
            OfdPort=7777,
        )

        kkm.AddDevice()

        return kkm
