from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from rbsoftskkm.dto.operations.sender_info import SenderInfo as _SenderInfo
from rbsoftskkm.dto.results.device import Device


@dataclass
class DeviceTaskInfo:
    """Информация о задаче устройства."""

    #: Тип задания.
    TaskType: int = 0

    #: Идентификатор документа.
    DocId: str = ""

    #: Дата создания / выполнения операции.
    Date: datetime = datetime.min

    #: Идентификатор документа-основания.
    BaseDocId: str = ""

    #: Идентификатор запроса.
    RequestId: str = ""

    #: Идентификатор терминала.
    TerminalId: str = ""

    #: Имя устройства.
    DeviceName: str = ""

    #: Идентификатор пула.
    PoolId: str = ""

    #: Код результата (0 — успех).
    ResultCode: int = 0

    #: Описание результата.
    ResultDescription: str = ""

    #: Признак успешного завершения обработки.
    Processed: bool = False

    #: Версия клиента.
    ClientVersion: str = ""

    #: Версия сервера.
    ServerVersion: str = ""

    #: Сведения об устройстве, обработавшем задание.
    DeviceInfo: Optional[Device] = None

    #: XML-представление документа.
    Xml: str = ""

    #: Сведения о приложении-источнике запроса.
    SenderInfo: Optional[_SenderInfo] = None
