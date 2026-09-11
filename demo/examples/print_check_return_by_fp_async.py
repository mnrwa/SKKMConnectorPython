from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    Customer,
    FiscalLine,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class PrintCheckReturnByFpAsync(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Асинхронная печать чека возврата по ФП"

    def PostPrintCheckReturnByFpAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.SaleReturn
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.Electronically = False
        kkm.AdditionalAttribute = "1775661887"
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Email="kuznicov@mail.ru", Vatin="500100732259")

        kkm.Payments = Payments(
            Cash=Decimal("90"),
            ElectronicPayment=Decimal("0"),
            AdvancePayment=Decimal("0"),
            Credit=Decimal("0"),
            CashProvision=Decimal("0"),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("73.18"),
                Sum=Decimal("73.18"),
                DiscountSum=Decimal("0"),
                Department=1,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Service,
            ),
        )

        kkm.PrintCheckAsync()

        return kkm
