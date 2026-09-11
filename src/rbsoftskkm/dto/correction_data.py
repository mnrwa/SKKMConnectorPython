from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time

from rbsoftskkm.dto.enums.correction_types import CorrectionTypes


@dataclass
class CorrectionData:
    """Данные коррекции:

    Type - Тип коррекции. Используйте enum CorrectionTypes

    Description - Описание коррекции

    Date - Дата совершения корректируемого расчёта

    Number - Номер предписания налогового органа (для Type = ПоПредписанию)
    """

    #: Тип коррекции. Используйте enum CorrectionTypes.
    Type: CorrectionTypes = CorrectionTypes.Самостоятельно

    #: Описание коррекции.
    Description: str = ""

    #: Дата совершения корректируемого расчёта.
    Date: datetime = field(default_factory=lambda: datetime.combine(date.today(), time.min))

    #: Номер предписания налогового органа.
    Number: str = ""
