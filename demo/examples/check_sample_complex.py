from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    AgentType,
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
    Vendor,
)


class CheckSampleComplex(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Комплексный чек: товар, скидка, маркировка, частичное выбытие, подарочная карта, комиссия"

    def PostCheckSampleComplex(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Customer = Customer(
            Info="ООО 'Рога и Копыта'",
            Vatin="500100732259",
            Email="kuznicov@mail.ru",
        )

        # 1. Простой товар — без скидок, маркировки, агента.
        kkm.Positions.append(
            FiscalLine(
                Name="Батарейка АА, уп. 2шт.",
                Quantity=Decimal("2"),
                Price=Decimal("50"),
                Sum=Decimal("100"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
            ),
        )

        # 2. Строка со скидкой — DiscountSum заполнен, Sum меньше Price * Quantity.
        kkm.Positions.append(
            FiscalLine(
                Name="Кофе в зёрнах, 1кг",
                Quantity=Decimal("1"),
                Price=Decimal("800"),
                DiscountSum=Decimal("50"),
                Sum=Decimal("750"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
            ),
        )

        # 3. Маркированный, не подакцизный товар.
        kkm.Positions.append(
            FiscalLine(
                Name="Футболка хлопковая, р.M",
                Quantity=Decimal("1"),
                Price=Decimal("1200"),
                Sum=Decimal("1200"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="0",
                Marking=Marking(Gs1m="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno="),
                MarkingCode="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno=",
            ),
        )

        # 4. Частичное выбытие маркированной единицы: отрез 2 м из рулона 50 м.
        kkm.Positions.append(
            FiscalLine(
                Name="Ткань костюмная (рулон 50м)",
                Quantity=Decimal("2"),
                Price=Decimal("100"),
                Sum=Decimal("200"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="0",
                Marking=Marking(Gs1m="0104607010350246215Ds>JRjNE!jZ! 93dGVz"),
                MarkingCode="0104607010350246215Ds>JRjNE!jZ! 93dGVz",
                Fractional=FractionalQuantity(Numerator=2, Denominator=50),
            ),
        )

        # 5. Подарочная карта — по 54-ФЗ это аванс, а не товар.
        kkm.Positions.append(
            FiscalLine(
                Name="Подарочная карта номиналом 1000 руб.",
                Quantity=Decimal("1"),
                Price=Decimal("1000"),
                Sum=Decimal("1000"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Advance,
            ),
        )

        # 6. Комиссионный товар: признак агента и данные комитента.
        kkm.Positions.append(
            FiscalLine(
                Name="Часы наручные (комиссионный товар)",
                Quantity=Decimal("1"),
                Price=Decimal("3500"),
                Sum=Decimal("3500"),
                Tax="20",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                AgentSign=AgentType.Commissioner,
                Vendor=Vendor(
                    Name="ИП Сидоров Сидор Сидорович",
                    Vatin="500100732200",
                    Phones=["+79001234567"],
                ),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("3750"), ElectronicPayment=Decimal("3000"))

        kkm.PrintCheck()
        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
