from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, FiscalizationParameters, FiscalizationReasonCode, SkkmConnector


class Fiscalization(Sample):
    GroupPath = "Работа с ККМ|Фискализация"
    Title = "Фискализация кассы"
    SortOrder = 0

    def PostFiscalization(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)

        kkm.FiscalizationParameters = FiscalizationParameters(
            RnNumber="00031415926",
            Fn="0123123123123",
            CompanyName="ООО 'Ромашка'",
            Vatin="7722345678",
            SaleAddress="г.Улан-Удэ, ул.Виноградная, д11А, офис 25",
            SaleLocation="Офис",
            TaxationSystems="0,1,2,4,5",
            FfdVersionKkt="1.2",
            FfdVersionFn="1.2",
            IsEncrypted=False,
            IsOffline=False,
            IsBsoSign=True,
            RegistrationLabelCodes="3.1",
            ReasonCode=FiscalizationReasonCode.RequisitesChange,
            OfdName="Тестовый ОФД",
            OfdVatin="1234554321",
            FnsUrl="nalog.ru",
            SenderEmail="ivanov@mail.ru",
            IsMarking=True,
            IsExcisable=True,
        )

        kkm.Fiscalization()

        return kkm
