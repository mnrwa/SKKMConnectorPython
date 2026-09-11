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


class PrintCheckReturnAdvance(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Печать чека возврата аванса"

    def PostPrintCheckReturnAdvance(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.Electronically = False
        kkm.PaymentType = CheckType.SaleReturn
        kkm.TaxVariant = TaxSystem.УСНД_Р
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Vatin="500100732259", Email="kuznicov@mail.ru")

        kkm.Payments = Payments(
            AdvancePayment=Decimal("10"),
            Cash=Decimal("0"),
            CashProvision=Decimal("0"),
            Credit=Decimal("0"),
            ElectronicPayment=Decimal("0"),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10"),
                DiscountSum=Decimal("0"),
                Department=2,
                Tax="120",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.Advance,
            ),
        )

        kkm.PrintCheck()

        return kkm
