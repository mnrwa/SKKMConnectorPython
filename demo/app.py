"""Тёмная тема демо-приложения: палитра и таблица стилей."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPalette, QPixmap
from PySide6.QtWidgets import QApplication

WINDOW_BACKGROUND = "#17171A"
PANEL_BACKGROUND = "#1E1E22"
EDITOR_BACKGROUND = "#1B1B1F"
HEADER_BACKGROUND = "#232327"
BORDER = "#2C2C32"
SECTION_TEXT = "#7E7E86"
PRIMARY_TEXT = "#E6E6EA"
EDITOR_TEXT = "#DCDCDC"
ACCENT = "#3574F0"
ACCENT_HOVER = "#4B84F5"
SELECTION = "#2F4B7B"

METHOD_TEXT_COLORS = {
    "GET": "#6BAF5A",
    "POST": "#D19A66",
    "PUT": "#61AFEF",
    "DELETE": "#E06C75",
}

METHOD_PILL_COLORS = {
    "GET": "#3F8F53",
    "POST": "#C4703A",
    "PUT": "#3A7AB8",
    "DELETE": "#B84A52",
}

STATUS_OK = "#62C073"
STATUS_ERROR = "#E06C75"
STATUS_IDLE = "#7E7E86"

MONOSPACE = "Cascadia Code, Consolas, Courier New, monospace"

STYLE_SHEET = f"""
QWidget {{
    background-color: {WINDOW_BACKGROUND};
    color: {PRIMARY_TEXT};
    font-size: 13px;
}}

QLabel[section="true"] {{
    color: {SECTION_TEXT};
    font-size: 11px;
    font-weight: 600;
}}

QFrame[panel="true"] {{
    background-color: {PANEL_BACKGROUND};
    border: 1px solid {BORDER};
    border-radius: 6px;
}}

QFrame[editorPanel="true"] {{
    background-color: {EDITOR_BACKGROUND};
    border: 1px solid {BORDER};
    border-radius: 6px;
}}

QFrame[header="true"] {{
    background-color: {HEADER_BACKGROUND};
    border: none;
    border-bottom: 1px solid {BORDER};
}}

QLineEdit {{
    background-color: {EDITOR_BACKGROUND};
    border: 1px solid {BORDER};
    border-radius: 4px;
    padding: 5px 7px;
    selection-background-color: {SELECTION};
}}

QLineEdit:focus {{
    border: 1px solid #3D6185;
}}

QPlainTextEdit {{
    background-color: {EDITOR_BACKGROUND};
    color: {EDITOR_TEXT};
    border: none;
    padding: 8px 12px;
    selection-background-color: {SELECTION};
}}

QTreeWidget {{
    background-color: {EDITOR_BACKGROUND};
    border: 1px solid {BORDER};
    border-radius: 4px;
    outline: none;
}}

QTreeWidget::item {{
    min-height: 24px;
    padding: 2px 0;
    border-radius: 3px;
}}

QTreeWidget::item:selected {{
    background-color: {SELECTION};
    color: {PRIMARY_TEXT};
}}

QTreeWidget::item:hover {{
    background-color: #26262B;
}}

QPushButton {{
    background-color: #2A2A30;
    border: 1px solid {BORDER};
    border-radius: 4px;
    padding: 6px 16px;
}}

QPushButton:hover {{
    background-color: #33333A;
}}

QPushButton:disabled {{
    color: #5A5A62;
    background-color: #232328;
}}

QPushButton[accent="true"] {{
    background-color: {ACCENT};
    border: 1px solid {ACCENT};
    color: #FFFFFF;
    font-weight: 600;
}}

QPushButton[accent="true"]:hover {{
    background-color: {ACCENT_HOVER};
}}

QPushButton[accent="true"]:disabled {{
    background-color: #2C3A55;
    border-color: #2C3A55;
    color: #7F8A9C;
}}

QPushButton[iconButton="true"] {{
    padding: 3px;
    min-width: 24px;
    background-color: transparent;
    border: none;
}}

QPushButton[iconButton="true"]:hover {{
    background-color: #33333A;
}}

QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background: #3A3A42;
    border-radius: 5px;
    min-height: 24px;
}}

QScrollBar::handle:vertical:hover {{
    background: #4A4A54;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 10px;
    margin: 0;
}}

QScrollBar::handle:horizontal {{
    background: #3A3A42;
    border-radius: 5px;
    min-width: 24px;
}}

QScrollBar::add-line, QScrollBar::sub-line {{
    width: 0;
    height: 0;
}}

QScrollBar::add-page, QScrollBar::sub-page {{
    background: transparent;
}}

QSplitter::handle {{
    background-color: transparent;
}}

QToolTip {{
    background-color: #252526;
    color: #D4D4D4;
    border: 1px solid #454545;
    padding: 6px 8px;
}}
"""

COPY_ICON_PATH = (
    "M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11"
    "c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"
)


def copy_icon(color: str = SECTION_TEXT, size: int = 16) -> QIcon:
    """Иконка Material ContentCopy, отрисованная из SVG."""
    from PySide6.QtSvg import QSvgRenderer

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="{size}" height="{size}">'
        f'<path fill="{color}" d="{COPY_ICON_PATH}"/></svg>'
    ).encode("utf-8")

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    QSvgRenderer(svg).render(painter)
    painter.end()
    return QIcon(pixmap)


def apply_theme(app: QApplication) -> None:
    """Тёмная палитра и стили: отдельная библиотека тем не нужна."""
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(WINDOW_BACKGROUND))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(PRIMARY_TEXT))
    palette.setColor(QPalette.ColorRole.Base, QColor(EDITOR_BACKGROUND))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(PANEL_BACKGROUND))
    palette.setColor(QPalette.ColorRole.Text, QColor(PRIMARY_TEXT))
    palette.setColor(QPalette.ColorRole.Button, QColor(PANEL_BACKGROUND))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(PRIMARY_TEXT))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(SELECTION))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(PRIMARY_TEXT))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#252526"))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#D4D4D4"))
    app.setPalette(palette)
    app.setStyleSheet(STYLE_SHEET)
