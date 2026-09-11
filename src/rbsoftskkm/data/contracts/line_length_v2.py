from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LineLengthV2:
    """Ширина строки чека."""

    #: Ширина строки чека в символах.
    LineLength: int = 0

    #: Ширина печатной области в пикселях.
    LineLengthPixels: int = 0
