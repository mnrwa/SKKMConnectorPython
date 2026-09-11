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


class PrintCheckReturn(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Печать чека возврата"

    def PostPrintCheckReturn(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.SaleReturn
        kkm.TaxVariant = TaxSystem.УСН
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Email="kuznicov@mail.ru", Vatin="500100732259")
        kkm.Payments = Payments(Cash=Decimal("90"))

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1"),
                MeasurementUnit="шт",
                Price=Decimal("60"),
                Sum=Decimal("60"),
                DiscountSum=Decimal("0"),
                Department=1,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.Advance,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="SIMTEK манжета переходная D50х32",
                Quantity=Decimal("1"),
                MeasurementUnit="шт",
                Price=Decimal("21.85"),
                Sum=Decimal("21.85"),
                DiscountSum=Decimal("0"),
                Department=1,
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.Advance,
            ),
        )

        kkm.PrintCheck()

        return kkm
