from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Marking:
    """Код товарной номенклатуры / маркировка позиции.
    Создайте объект и заполните нужные поля (MarkingCode/Code, Gtin, StampType, Quantity и т.д.),
    затем присвойте в Marking.
    """

    #: Глобальный идентификатор торговой единицы (GTIN)
    Gtin: Optional[str] = None

    #: Тип маркировки. Список значений:
    #: "02" – изделия из меха
    #: "05" - табачная продукция
    #: "1520" - обувные товары
    StampType: Optional[str] = None

    #: Контрольный идентификационный знак (КиЗ)
    Stamp: Optional[str] = None

    #: Серийный номер
    SerialNumber: Optional[str] = None

    #: Код контрольной марки. Кодируется текстом в кодировке Base64
    Code: Optional[str] = field(default=None, metadata={"json": "MarkingCode"})

    #: Штрихкод
    Barcode: Optional[str] = None

    #: Тип (группа) товара
    CommodityGroup: Optional[str] = None

    #: Код товара, формат которого не идентифицирован в Base64
    NotIdentified: Optional[str] = None

    #: Код товара в формате EAN-8 в Base64
    Ean8: Optional[str] = field(default=None, metadata={"json": "EAN8"})

    #: Код товара в формате EAN-13 в Base64
    Ean13: Optional[str] = field(default=None, metadata={"json": "EAN13"})

    #: Код товара в формате ITF-14 в Base64
    Itf14: Optional[str] = field(default=None, metadata={"json": "ITF14"})

    #: Код товара в формате GS1, нанесенный на товар, не подлежащий маркировке средствами идентификации в Base64
    Gs10: Optional[str] = field(default=None, metadata={"json": "GS10"})

    #: Код товара в формате GS1, нанесенный на товар, подлежащий маркировке средствами идентификации в Base64
    Gs1m: Optional[str] = field(default=None, metadata={"json": "GS1M"})

    #: Код товара в формате короткого кода маркировки, нанесенный на товар, подлежащий маркировке средствами идентификации в Base64
    Kmk: Optional[str] = field(default=None, metadata={"json": "KMK"})

    #: Контрольно-идентификационный знак мехового изделия
    Mi: Optional[str] = field(default=None, metadata={"json": "MI"})

    #: Код товара в формате ЕГАИС-2.0 в Base64
    Egais20: Optional[str] = field(default=None, metadata={"json": "EGAIS20"})

    #: Код товара в формате ЕГАИС-3.0 в Base64
    Egais30: Optional[str] = field(default=None, metadata={"json": "EGAIS30"})

    #: Код товара в формате Ф.1 в Base64
    F1: Optional[str] = None

    #: Код товара в формате Ф.2 в Base64
    F2: Optional[str] = None

    #: Код товара в формате Ф.3 в Base64
    F3: Optional[str] = None

    #: Код товара в формате Ф.4 в Base64
    F4: Optional[str] = None

    #: Код товара в формате Ф.5 в Base64
    F5: Optional[str] = None

    #: Код товара в формате Ф.6 в Base64
    F6: Optional[str] = None
