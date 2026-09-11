from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Agent,
    AgentType,
    Cashier,
    CheckType,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    Vendor,
)


class CheckSample13(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Данные агент и поставщика в позиции"

    def PostCheckSample13(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("120"),
                Sum=Decimal("120.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                Agent=Agent(
                    PayingAgentOperation="Приём платежей",
                    PayingAgentPhone=["+79001234567"],
                    ReceivePaymentsOperatorPhone=["+79001234567"],
                ),
                Vendor=Vendor(Name="ООО Ромашка", Phones=["+79001234567"], Vatin="7701234560"),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("120.0"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
