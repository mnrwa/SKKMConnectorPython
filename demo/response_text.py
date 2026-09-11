"""Ответ сервера в том же виде, что приходит по HTTP."""

from __future__ import annotations

from typing import Any

from rbsoftskkm import SkkmConnector
from rbsoftskkm.data import json_codec


def format_response(kkm: SkkmConnector) -> str:
    envelope: dict[str, Any] = {}
    if kkm.LastResult is not None:
        envelope["Result"] = kkm.LastResult
    envelope["Code"] = kkm.ErrorCode
    envelope["Description"] = kkm.ErrorDescription
    envelope["Success"] = kkm.Ok
    return json_codec.dumps(envelope)
