from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.dto.enums.fiscalization_reason_code import FiscalizationReasonCode


@dataclass
class FiscalizationRequest(CheckbaseParameters):
    """Тело запроса фискализации ККТ."""

    #: Регистрационный номер ККТ.
    RnNumber: Optional[str] = None

    #: Коды систем налогообложения через запятую.
    TaxationSystems: Optional[str] = None

    #: ИНН организации.
    Vatin: Optional[str] = None

    #: Название организации.
    CompanyName: Optional[str] = None

    #: Заводской номер ФН.
    Fn: Optional[str] = None

    #: Версия ФФД ККТ.
    FfdVersionKkt: Optional[str] = None

    #: Версия ФФД ФН.
    FfdVersionFn: Optional[str] = None

    #: Коды причин изменения сведений о ККТ.
    RegistrationLabelCodes: Optional[str] = None

    #: Адрес ОФД.
    OfdAddress: Optional[str] = None

    #: Порт ОФД.
    OfdPort: Optional[int] = None

    #: Номер автоматического устройства для расчётов.
    AutomaticNumber: Optional[str] = None

    #: Email отправителя чека.
    SenderEmail: Optional[str] = None

    #: Код причины перерегистрации.
    ReasonCode: Optional[FiscalizationReasonCode] = None

    #: Хост ИСМ.
    IsmHost: Optional[str] = None

    #: Порт ИСМ.
    IsmPort: Optional[int] = None

    #: Адрес сайта ФНС.
    FnsUrl: Optional[str] = None

    #: ИНН ОФД.
    OfdVatin: Optional[str] = None

    #: Название ОФД.
    OfdName: Optional[str] = None

    #: Коды признаков агента через запятую.
    AgentTypes: Optional[str] = None

    #: Признак формирования АС БСО.
    IsBsoSign: Optional[bool] = None

    #: Признак торговли маркированными товарами.
    IsMarking: Optional[bool] = None

    #: Признак ломбардной деятельности.
    IsPawnshop: Optional[bool] = None

    #: Признак страховой деятельности.
    IsAssurance: Optional[bool] = None

    #: Признак автоматического режима.
    IsAutomatic: Optional[bool] = None

    #: Признак применения в торговом автомате.
    IsVending: Optional[bool] = None

    #: Признак установки принтера в автомате.
    IsAutomaticPrinter: Optional[bool] = None

    #: Признак расчётов только в интернете.
    IsOnline: Optional[bool] = None

    #: Признак проведения лотерей.
    IsLottery: Optional[bool] = None

    #: Признак проведения азартных игр.
    IsGambling: Optional[bool] = None

    #: Признак продажи подакцизных товаров.
    IsExcisable: Optional[bool] = None

    #: Признак расчётов за услуги.
    IsService: Optional[bool] = None

    #: Признак шифрования данных.
    IsEncrypted: Optional[bool] = None

    #: Признак автономного режима.
    IsOffline: Optional[bool] = None

    #: Признак общественного питания.
    IsCateringServices: Optional[bool] = None

    #: Признак оптовой торговли.
    IsWholesaleTrade: Optional[bool] = None

    #: Адрес расчётов.
    SaleAddress: Optional[str] = None

    #: Место расчётов.
    SaleLocation: Optional[str] = None
