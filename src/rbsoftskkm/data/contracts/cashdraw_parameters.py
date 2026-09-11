from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters


@dataclass
class CashdrawParameters(CheckbaseParameters):
    """Внесения/выемки наличных."""

    #: Сумма внесения или выемки
    Sum: Decimal = Decimal("0")
