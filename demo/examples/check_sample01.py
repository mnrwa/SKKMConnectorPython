from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    Customer,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample01(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Продажа (базовый чек)"

    def PostCheckSample01(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ЕНВД
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Vatin="500100732259", Email="kuznicov@mail.ru")

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("30"),
                Sum=Decimal("30"),
                DiscountSum=Decimal("0"),
                Department=1,
                Tax="20",
                TaxSum=Decimal("5"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(
            Cash=Decimal("30"),
            ElectronicPayment=Decimal("0"),
            AdvancePayment=Decimal("0"),
            Credit=Decimal("0"),
            CashProvision=Decimal("0"),
        )

        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
