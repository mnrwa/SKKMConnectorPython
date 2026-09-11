from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Agent,
    AgentType,
    BarcodeLine,
    Cashier,
    CheckTimeZone,
    CheckType,
    Customer,
    ElectronicPayment,
    ElectronicPaymentMethod,
    FiscalLine,
    FractionalQuantity,
    Industry,
    LineStyle,
    Marking,
    MeasureOfQuantity,
    OperationalAttribute,
    Payments,
    PictureAlignment,
    PictureLine,
    SeparatorLine,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    TextLine,
    UserAttribute,
    Vendor,
)


class checkSampleUltimate(Sample):
    """Комплексный чек: объекты расчёта, НДС, агент, маркировка, безнал, нефискальные строки."""

    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Комплексный чек: все объекты, НДС, агент, маркировка"

    def PostComplexCheck(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name="Иванов И. И.", Vatin="500100732259")
        kkm.NewRequest()
        kkm.DocumentId = "a7c4e2b1-9d58-4f06-8c3a-1b2e4d6f8091"
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.TimeZone = CheckTimeZone.MskPlus5
        kkm.SenderEmail = "ivanov@mail.ru"
        kkm.SaleAddress = "г. Москва, ул. Ленина, д. 1"
        kkm.SaleLocation = "https://shop.ru"
        kkm.TextBefore = "Текст 1"
        kkm.TextAfter = "Текст 2"

        kkm.Customer = Customer(
            Info="ООО Ромашка",
            Vatin="7701234560",
            Email="ivanov@mail.ru",
            Phone="+79001234567",
            DateOfBirth="01.01.1990",
            Citizenship="643",
            DocumentTypeCode="21",
            DocumentData="4509 123456",
            Address="г. Москва, ул. Ленина, д. 1",
        )

        kkm.AgentSign = AgentType.Agent

        kkm.Agent = Agent(
            PayingAgentOperation="Приём платежей",
            PayingAgentPhone=["+79001234567"],
            ReceivePaymentsOperatorPhone=["+79001234567"],
            MoneyTransferOperatorPhone=["+79001234567"],
            MoneyTransferOperatorName="ООО Рога и копыта",
            MoneyTransferOperatorAddress="г. Москва, ул. Ленина, д. 1",
            MoneyTransferOperatorVatin="7701234560",
        )

        kkm.Vendor = Vendor(Name="ООО Ромашка", Vatin="7701234560", Phones=["+79001234567", "+79007654321"])
        kkm.UserAttribute = UserAttribute(Name="НомерЗаказа", Value="42")

        kkm.OperationalAttribute = OperationalAttribute(
            DateTime="03.09.2026",
            OperationId=42,
            OperationData="Оплата по договору",
        )

        kkm.IndustryAttribute = Industry(
            IdentifierFoiv="030",
            DocumentDate="21.11.2023",
            DocumentNumber="1944",
            AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.FullPrepayment,
                Identifiers="M=0",
                AdditionalInformation="Не определено",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.PartialPrepayment,
                Identifiers="M=1",
                AdditionalInformation="Банковская карта",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.Advance,
                Identifiers="M=2",
                AdditionalInformation="СБП",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.FullPayment,
                Identifiers="RRN=123456789012",
                AdditionalInformation="Карта *1234",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.PartialPaymentAndCredit,
                Identifiers="M=4",
                AdditionalInformation="Перевод с банка",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.CreditTransfer,
                Identifiers="M=5",
                AdditionalInformation="Эл. кошелёк",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.CreditPayment,
                Identifiers="M=6",
                AdditionalInformation="Иной безнал",
            ),
        )

        kkm.Positions.append(
            TextLine(
                Text="[center]Комплексный чек: объекты, НДС, агент, маркировка",
                Alignment="center",
                Font="Big",
            ),
        )

        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Dotted))

        kkm.Positions.append(
            FiscalLine(
                Name="Товар",
                Quantity=Decimal("2"),
                Price=Decimal("6"),
                Sum=Decimal("10.0"),
                DiscountSum=Decimal("2"),
                Tax="none",
                TaxSum=Decimal("0"),
                Department=1,
                ProductCode="2208 20 290 0",
                AdditionalAttribute="Доп. реквизит товара",
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Agent=Agent(
                    PayingAgentOperation="Приём платежей",
                    PayingAgentPhone=["+79001234567"],
                    ReceivePaymentsOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorName="ООО Рога и копыта",
                    MoneyTransferOperatorAddress="г. Москва, ул. Ленина, д. 1",
                    MoneyTransferOperatorVatin="7701234560",
                ),
                Vendor=Vendor(Name="ООО Ромашка", Vatin="7701234560", Phones=["+79001234567", "+79007654321"]),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Подакцизный товар",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                DiscountSum=Decimal("0"),
                Tax="20",
                TaxSum=Decimal("1.67"),
                Department=2,
                ProductCode="2402 20 900 0",
                AdditionalAttribute="Подакциз",
                ExciseAmount=Decimal("5.5"),
                CountryOfOrigin="643",
                CustomsDeclaration="10009100/220211/0001122",
                SignMethodCalculation=SignMethodCalculation.PartialPrepayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                Agent=Agent(
                    PayingAgentOperation="Приём платежей",
                    PayingAgentPhone=["+79001234567"],
                    ReceivePaymentsOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorName="ООО Рога и копыта",
                    MoneyTransferOperatorAddress="г. Москва, ул. Ленина, д. 1",
                    MoneyTransferOperatorVatin="7701234560",
                ),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Работа",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="5",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.Work,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                Vendor=Vendor(Name="ООО Ромашка", Vatin="7701234560", Phones=["+79001234567", "+79007654321"]),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Услуга",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="5/105",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Service,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                Agent=Agent(
                    PayingAgentOperation="Приём платежей",
                    PayingAgentPhone=["+79001234567"],
                    ReceivePaymentsOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorPhone=["+79001234567"],
                    MoneyTransferOperatorName="ООО Рога и копыта",
                    MoneyTransferOperatorAddress="г. Москва, ул. Ленина, д. 1",
                    MoneyTransferOperatorVatin="7701234560",
                ),
                Vendor=Vendor(Name="ООО Ромашка", Vatin="7701234560", Phones=["+79001234567", "+79007654321"]),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Ставка азартной игры",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="7",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.GamblingStake,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выигрыш азартной игры",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="7/107",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditTransfer,
                SignCalculationObject=SignCalculationObject.GamblingPrize,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Лотерейный билет",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditPayment,
                SignCalculationObject=SignCalculationObject.LotteryTicket,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выигрыш лотереи",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10/110",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.LotteryPrize,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Предоставление РИД",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="18",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPrepayment,
                SignCalculationObject=SignCalculationObject.IntellectualProperty,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Платёж",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="18/118",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.Advance,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Агентское вознаграждение",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.AgentFee,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Составной предмет расчёта",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20/120",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.Payout,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Иной предмет расчёта",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="22",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditTransfer,
                SignCalculationObject=SignCalculationObject.Other,
                MeasureOfQuantity=MeasureOfQuantity.Other,
                MeasurementUnit="255",
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Имущественное право",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="22/122",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditPayment,
                SignCalculationObject=SignCalculationObject.PropertyRight,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Внереализационный доход",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.NonOperatingIncome,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Страховые взносы",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="0",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPrepayment,
                SignCalculationObject=SignCalculationObject.OtherPayments,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Торговый сбор",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="5",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.TradeFee,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Курортный сбор",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="5/105",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.TouristTax,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Залог",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="7",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.Deposit,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Расход",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="7/107",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditTransfer,
                SignCalculationObject=SignCalculationObject.Expense,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОПС ИП",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditPayment,
                SignCalculationObject=SignCalculationObject.PensionContributionIp,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОПС",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10/110",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.PensionContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОМС ИП",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="18",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPrepayment,
                SignCalculationObject=SignCalculationObject.MedicalContributionIp,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОМС",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="18/118",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.MedicalContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОСС",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.SocialContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Платёж казино",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20/120",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.CasinoPayment,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выдача денежных средств",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="22",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditTransfer,
                SignCalculationObject=SignCalculationObject.CashWithdrawalByAgent,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="АТНМ",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20",
                TaxSum=Decimal("1.67"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.АТНМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                ExciseAmount=Decimal("12.3"),
                CountryOfOrigin="276",
                CustomsDeclaration="10009100/140923/0001122",
                ProductCode="2208 20 290 0",
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="АТМ",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="20",
                TaxSum=Decimal("1.67"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.АТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                ExciseAmount=Decimal("185.4"),
                CountryOfOrigin="276",
                CustomsDeclaration="10009100/140923/0001122",
                ProductCode="2208 20 290 0",
                AdditionalAttribute="Импорт АТМ",
                Marking=Marking(
                    Code="MDEwNDYwMTkwNzAwMjgwNTIxNUR0RDJReUlCSjVrYR05MUYwMTMdOTJnajR4alVwdzlCZHVLUXZhT3pNYmFyeGhkVFRqWmp1cFR0RkFZOTl0WmhVPQ==",
                    Gtin="04601907002805",
                    StampType="05",
                    SerialNumber="DtD2QyIBJ5ka",
                ),
                Industry=Industry(
                    IdentifierFoiv="030",
                    DocumentDate="21.11.2023",
                    DocumentNumber="1944",
                    AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
                ),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="ТНМ",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТНМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                ProductCode="0402 10 190 0",
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="ТМ",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="10",
                TaxSum=Decimal("0.91"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.Agent,
                MarkingCode="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno=",
                Fractional=FractionalQuantity(Numerator=1, Denominator=4),
                Industry=Industry(
                    IdentifierFoiv="030",
                    DocumentDate="21.11.2023",
                    DocumentNumber="1944",
                    AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
                ),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Сыр",
                Quantity=Decimal("0.5"),
                Price=Decimal("20"),
                Sum=Decimal("10.0"),
                Tax="10",
                TaxSum=Decimal("0.91"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
                MeasurementUnit="11",
                AgentSign=AgentType.Agent,
                Marking=Marking(Code="MDEwNDYwMjIyMDAwNjU0OTIxNW9wRmNtSx05M2RHVno="),
                Industry=Industry(
                    IdentifierFoiv="030",
                    DocumentDate="21.11.2023",
                    DocumentNumber="1944",
                    AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
                ),
            ),
        )

        kkm.Positions.append(BarcodeLine(Type="CODE128", Barcode="ABC-12345", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="QR", Barcode="https://shop.ru", Alignment="center"))

        kkm.Positions.append(
            PictureLine(
                Value="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
                Alignment=PictureAlignment.Right,
            ),
        )

        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Dotted))

        kkm.Payments = Payments(
            Cash=Decimal("50"),
            ElectronicPayment=Decimal("70"),
            AdvancePayment=Decimal("70"),
            Credit=Decimal("70"),
            CashProvision=Decimal("60"),
        )

        kkm.PrintCheck()

        return kkm
