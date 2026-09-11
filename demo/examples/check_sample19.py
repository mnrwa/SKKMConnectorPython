from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    Customer,
    FiscalLine,
    FractionalQuantity,
    Marking,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample19(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Дробное количество маркированного товара"

    def PostCheckSample19(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.УСН
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Vatin="500100732259", Email="kuznicov@mail.ru")

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1.234"),
                Price=Decimal("750.0"),
                Sum=Decimal("750.0"),
                Department=2,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="0",
                Marking=Marking(Gs1m="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno="),
                Fractional=FractionalQuantity(Numerator=1, Denominator=208),
            ),
        )

        kkm.Payments = Payments(
            Cash=Decimal("750.0"),
            ElectronicPayment=Decimal("0.0"),
            AdvancePayment=Decimal("0.0"),
            Credit=Decimal("0.0"),
            CashProvision=Decimal("0.0"),
        )

        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
