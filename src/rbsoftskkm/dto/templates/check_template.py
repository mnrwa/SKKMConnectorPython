from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.templates.check_template_document import CheckTemplateDocument


@dataclass
class CheckTemplate:
    """Шаблон чека, полученный с сервера."""

    #: Идентификатор шаблона на сервере.
    Id: str = ""

    #: Имя шаблона чека.
    Name: str = ""

    #: Документ шаблона.
    Document: Optional[CheckTemplateDocument] = None
