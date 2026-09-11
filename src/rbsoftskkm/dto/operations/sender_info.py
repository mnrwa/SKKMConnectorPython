from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SenderInfo:
    """Сведения о приложении-источнике запроса."""

    #: Название приложения.
    AppName: str = ""

    #: Версия приложения.
    AppVersion: str = ""
