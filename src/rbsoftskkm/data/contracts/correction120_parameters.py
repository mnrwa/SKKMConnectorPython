from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.check_parameters import CheckParameters
from rbsoftskkm.dto.correction_data import CorrectionData as _CorrectionData


@dataclass
class Correction120Parameters(CheckParameters):
    """Тело запроса печати чека коррекции ФФД 1.2."""

    #: Данные корректировки
    CorrectionData: Optional[_CorrectionData] = None
