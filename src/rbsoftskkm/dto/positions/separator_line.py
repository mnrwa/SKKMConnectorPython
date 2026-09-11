from __future__ import annotations

from dataclasses import dataclass, field

from rbsoftskkm.dto.enums.line_style import LineStyle as _LineStyle
from rbsoftskkm.dto.positions.position import Position


@dataclass
class SeparatorLine(Position):
    """Разделительная линия в чеке:

    LineStyle - Стиль. Используйте enum LineStyle
    """

    #: Стиль разделительной линии. Используйте enum LineStyle.
    LineStyle: _LineStyle = field(default=_LineStyle.Solid, metadata={"json": "lineStyle"})
