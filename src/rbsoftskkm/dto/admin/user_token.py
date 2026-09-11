from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class UserToken:
    """Токен авторизации пользователя."""

    TokenId: str = field(default="", metadata={"json": "tokenId"})

    Expire: str = field(default="", metadata={"json": "expire"})
