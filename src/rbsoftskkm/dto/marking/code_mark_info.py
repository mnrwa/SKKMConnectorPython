from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CodeMarkInfo:
    """Сведения о коде маркировки."""

    #: Полный код маркировки (КиЗ).
    Cis: str = ""

    #: Признак валидности структуры кода.
    Valid: bool = False

    #: Код маркировки без крипто-подписи.
    PrintView: str = ""

    #: Идентификаторы товарных групп.
    GroupIds: list[int] = field(default_factory=list)

    #: Результат криптографической проверки кода.
    Verified: bool = False

    #: Признак статуса «В обороте».
    Realizable: bool = False

    #: Признак нанесения кода на упаковку.
    Utilised: bool = False

    #: Признак наличия кода в ГИС МТ.
    Found: bool = False

    #: Код ошибки проверки.
    ErrorCode: int = 0

    #: Сообщение об ошибке.
    Message: str = ""

    #: Признак старта прослеживаемости в товарной группе.
    IsTracking: bool = False

    #: Признак того, что товар с данным кодом уже продан.
    Sold: bool = False

    #: Код товара (GTIN).
    Gtin: str = ""

    #: Тип упаковки.
    PackageType: str = ""

    #: ИНН производителя.
    ProducerInn: str = ""

    #: Признак нахождения продукции в «серой зоне».
    GrayZone: bool = False

    #: Признак блокировки кода по решению ОГВ.
    IsBlocked: bool = False

    #: Признак некорректного (незарегистрированного) GTIN.
    IsGreyGtin: bool = False

    #: Органы государственной власти, установившие блокировку.
    Ogvs: list[str] = field(default_factory=list)

    #: Ёмкость КИГУ (количество потенциальных вложений).
    PackageQuantity: int = 0
