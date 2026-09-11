from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.enums.agent_type import AgentType
from rbsoftskkm.dto.enums.measure_of_quantity import MeasureOfQuantity as _MeasureOfQuantity
from rbsoftskkm.dto.enums.sign_calculation_object import SignCalculationObject as _SignCalculationObject
from rbsoftskkm.dto.enums.sign_method_calculation import SignMethodCalculation as _SignMethodCalculation
from rbsoftskkm.dto.positions.agent import Agent as _Agent
from rbsoftskkm.dto.positions.fractional_quantity import FractionalQuantity
from rbsoftskkm.dto.positions.industry import Industry as _Industry
from rbsoftskkm.dto.positions.marking import Marking as _Marking
from rbsoftskkm.dto.positions.position import Position
from rbsoftskkm.dto.positions.vendor import Vendor as _Vendor


@dataclass
class FiscalLine(Position):
    """Фискальная строка чека (товар / услуга). Основные поля: Name, Quantity, Price, Sum,
    Tax, SignMethodCalculation, SignCalculationObject; при необходимости Marking, Agent, Vendor.
    """

    #: Наименование товара
    Name: str = ""

    #: Код товара
    ProductCode: Optional[str] = None

    #: Количество товара
    Quantity: Decimal = Decimal("1")

    #: Цена единицы товара с учетом скидок/наценок
    Price: Decimal = field(default=Decimal("0"), metadata={"json": "PriceWithDiscount"})

    #: Конечная сумма по позиции чека с учетом всех скидок/наценок
    Sum: Decimal = field(default=Decimal("0"), metadata={"json": "SumWithDiscount"})

    #: Сумма скидок и наценок
    DiscountSum: Decimal = Decimal("0")

    #: Ставка НДС. Обязательна: сервер отклоняет позицию без ставки
    Tax: str = ""

    #: Сумма НДС за предмет расчета
    TaxSum: Decimal = Decimal("0")

    #: Отдел, по которому ведется продажа
    Department: int = 0

    #: Признак способа расчёта. Используйте enum SignMethodCalculation.
    SignMethodCalculation: Optional[_SignMethodCalculation] = None

    #: Признак предмета расчёта. Используйте enum SignCalculationObject.
    SignCalculationObject: Optional[_SignCalculationObject] = None

    #: Единица измерения предмета расчета
    MeasurementUnit: Optional[str] = None

    #: Мера количества предмета расчёта. Используйте enum MeasureOfQuantity.
    MeasureOfQuantity: Optional[_MeasureOfQuantity] = None

    #: Сумма акциза с учетом копеек
    ExciseAmount: Optional[Decimal] = None

    #: Цифровой код страны происхождения товара
    CountryOfOrigin: Optional[str] = None

    #: Регистрационный номер таможенной декларации
    CustomsDeclaration: Optional[str] = None

    #: Признак агента по предмету расчёта. Используйте enum AgentType.
    AgentSign: Optional[AgentType] = field(default=None, metadata={"json": "SignSubjectCalculationAgent"})

    #: Данные агента. Создайте объект Agent и заполните нужные поля.
    Agent: Optional[_Agent] = field(default=None, metadata={"json": "AgentData"})

    #: Данные поставщика. Создайте объект Vendor
    #: (Name, Phones, Vatin).
    Vendor: Optional[_Vendor] = None

    #: Данные кода товарной номенклатуры. Создайте объект Marking.
    Marking: Optional[_Marking] = field(default=None, metadata={"json": "GoodCodeData"})

    #: Код контрольной марки
    MarkingCode: Optional[str] = None

    #: Описание частичного выбытия. Создайте объект FractionalQuantity
    #: (Numerator, Denominator).
    Fractional: Optional[FractionalQuantity] = field(default=None, metadata={"json": "FractionalQuantity"})

    #: Отраслевой реквизит. Создайте объект Industry
    #: (IdentifierFoiv, DocumentDate, DocumentNumber, AttributeValue).
    Industry: Optional[_Industry] = field(default=None, metadata={"json": "IndustryAttribute"})

    #: Дополнительный реквизит предмета расчета
    AdditionalAttribute: Optional[str] = None
