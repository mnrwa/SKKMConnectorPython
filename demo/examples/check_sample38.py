from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    ElectronicPayment,
    ElectronicPaymentMethod,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample38(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Сведения об оплате безналичными"

    def PostCheckSample38(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("60"),
                PaymentMethod=ElectronicPaymentMethod.FullPayment,
                Identifiers="RRN=123456789012",
                AdditionalInformation="Карта *1234",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("40"),
                PaymentMethod=ElectronicPaymentMethod.FullPayment,
                Identifiers="RRN=987654321000",
                AdditionalInformation="СБП",
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(ElectronicPayment=Decimal("100"))
        kkm.PrintCheck()

        return kkm
