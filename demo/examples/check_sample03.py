from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckTimeZone,
    CheckType,
    Customer,
    FiscalLine,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample03(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Часовая зона"

    def PostCheckSample03(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.TimeZone = CheckTimeZone.MskPlus7
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Vatin="500100732259", Email="kuznicov@mail.ru")

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("2"),
                Price=Decimal("50"),
                Sum=Decimal("100"),
                Department=0,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.Advance,
                MeasurementUnit="50",
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("50"), ElectronicPayment=Decimal("90.00"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
