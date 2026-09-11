from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.templates.check_template_document import CheckTemplateDocument


@dataclass
class CheckTemplateParameters:
    """Параметры создания или изменения шаблона чека:

    Name - Уникальное имя шаблона на сервере

    Document - Документ шаблона (CheckTemplateDocument)
    """

    #: Имя шаблона чека. Уникальный идентификатор на сервере.
    #: Разрешены символы a-z, A-Z, 0-9, _, -, (, ). Пробелы запрещены.
    Name: str = ""

    #: Документ шаблона
    Document: Optional[CheckTemplateDocument] = None
