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


class CheckSample02(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Подакцизный товар"

    def PostCheckSample02(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.УСН
        kkm.Electronically = True
        kkm.Customer = Customer(Info="ООО 'Рога и Копыта'", Vatin="500100732259", Email="kuznicov@mail.ru")

        kkm.Positions.append(
            FiscalLine(
                Name="Бутылка с водой 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10"),
                Department=0,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
                ExciseAmount=Decimal("1"),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Пиво",
                Quantity=Decimal("3"),
                Price=Decimal("10.50"),
                Sum=Decimal("31.50"),
                Department=1,
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("100.01"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
