from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import (
    BarcodePrintText,
    BarcodeType,
    LineStyle,
    Picture,
    PictureAlignment,
    PrintAlignment,
    PrintFont,
    PrintFormBarcode,
    PrintLine,
    PrintLineType,
    PrintTemplateType,
    SeparatorLine,
    SkkmConnector,
    TemplateItem,
    TemplateParameters,
)


class UpdateTemplate(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Рекламные чеки"
    Title = "Редактирование шаблона печати"
    SortOrder = 1

    def PutUpdateTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.TemplateParameters = TemplateParameters(
            Name="name120",
            Type=PrintTemplateType.Advertisement,
            TemplateItems=[
                TemplateItem(
                    PrintLine=PrintLine(
                        Type=PrintLineType.Text,
                        Line="Текс222т",
                        LineRight="",
                        Alignment=PrintAlignment.Center,
                        Font=PrintFont.H1,
                        Wrap=True,
                    ),
                ),
                TemplateItem(
                    PrintLine=PrintLine(
                        Type=PrintLineType.Text,
                        Line="Сумма",
                        LineRight="1 250,00",
                        Alignment=PrintAlignment.Left,
                        Font=PrintFont.Normal,
                        Wrap=False,
                    ),
                ),
                TemplateItem(
                    PrintLine=PrintLine(
                        Type=PrintLineType.Separator,
                        SeparatorLine=SeparatorLine(LineStyle=LineStyle.Solid),
                    ),
                ),
                TemplateItem(
                    PrintLine=PrintLine(
                        Type=PrintLineType.Barcode,
                        Alignment=PrintAlignment.Center,
                        Barcode=PrintFormBarcode(
                            Type=BarcodeType.QR,
                            Value="https://www.rbsoft.ru/",
                            PrintText=BarcodePrintText.None_,
                            Height=30,
                            BarWidth=6,
                        ),
                    ),
                ),
                TemplateItem(
                    PrintLine=PrintLine(
                        Type=PrintLineType.Picture,
                        Alignment=PrintAlignment.Center,
                        Scale=100,
                        Picture=Picture(
                            PictureBase64="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==",
                            Alignment=PictureAlignment.Center,
                            Width=200,
                            Height=80,
                        ),
                    ),
                ),
            ],
        )

        kkm.UpdateTemplate()

        return kkm
