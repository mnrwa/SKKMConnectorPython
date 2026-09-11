from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from rbsoftskkm.data.response_result_base import ResponseResultBase


@dataclass
class ResponseResult(ResponseResultBase):
    """Ответ Сервера ККМ."""

    #: Полезная нагрузка ответа.
    Result: Any = field(default=None, metadata={"json": "Result"})
