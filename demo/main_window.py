"""Главное окно демо: коллекция запросов, исходник примера и ответ сервера."""

from __future__ import annotations

import traceback
from datetime import timedelta
from typing import Optional

from PySide6.QtCore import QEvent, QModelIndex, QObject, QPersistentModelIndex, QRunnable, Qt, QThreadPool, Signal
from PySide6.QtGui import QColor, QFont, QFontMetrics, QGuiApplication, QMouseEvent, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QStyle,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QToolTip,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from demo import app as theme
from demo.connection_settings import DATE_FORMAT, ConnectionSettings, today
from demo.response_text import format_response
from demo.ui import doc_lookup, example_source
from demo.ui.example_host import ExampleItem, ExampleRunner, ExampleTreeNode, build_tree
from demo.ui.json_highlighter import JsonHighlighter
from demo.ui.python_highlighter import PythonHighlighter
from rbsoftskkm import SkkmConnector

ITEM_ROLE = Qt.ItemDataRole.UserRole
METHOD_ROLE = Qt.ItemDataRole.UserRole + 1
METHOD_COLUMN_WIDTH = 44


class RequestDelegate(QStyledItemDelegate):
    """Лист дерева: слева метка метода цветом, справа название запроса."""

    def paint(  # noqa: N802 - имя из Qt
        self,
        painter: QPainter,
        option: QStyleOptionViewItem,
        index: QModelIndex | QPersistentModelIndex,
    ) -> None:
        method = index.data(METHOD_ROLE)
        if not method:
            super().paint(painter, option, index)
            return

        style_option = QStyleOptionViewItem(option)
        self.initStyleOption(style_option, index)
        style_option.text = ""
        widget = style_option.widget
        style = widget.style() if widget is not None else QApplication.style()
        style.drawControl(QStyle.ControlElement.CE_ItemViewItem, style_option, painter, widget)

        rect = style_option.rect
        painter.save()

        method_font = QFont(style_option.font)
        method_font.setPointSizeF(max(7.0, method_font.pointSizeF() - 1))
        method_font.setWeight(QFont.Weight.DemiBold)
        painter.setFont(method_font)
        painter.setPen(QColor(theme.METHOD_TEXT_COLORS.get(str(method), theme.METHOD_TEXT_COLORS["POST"])))
        painter.drawText(
            rect.adjusted(4, 0, 0, 0),
            int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter),
            str(method),
        )

        painter.setFont(style_option.font)
        painter.setPen(QColor(theme.PRIMARY_TEXT))
        title_rect = rect.adjusted(METHOD_COLUMN_WIDTH, 0, -6, 0)
        title = QFontMetrics(style_option.font).elidedText(
            str(index.data(Qt.ItemDataRole.DisplayRole)),
            Qt.TextElideMode.ElideRight,
            title_rect.width(),
        )
        painter.drawText(title_rect, int(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter), title)
        painter.restore()


class WorkerSignals(QObject):
    finished = Signal(object)
    failed = Signal(str)


class ExampleWorker(QRunnable):
    """Запрос выполняется в рабочем потоке, интерфейс не подвисает."""

    def __init__(self, example: ExampleItem) -> None:
        super().__init__()
        self.example = example
        self.signals = WorkerSignals()

    def run(self) -> None:
        try:
            self.signals.finished.emit(ExampleRunner.invoke(self.example))
        except Exception:
            self.signals.failed.emit(traceback.format_exc())


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Демо SkkmConnector")
        self.resize(1200, 740)
        self.setMinimumSize(880, 520)

        self._connection = ConnectionSettings()
        self._selected: Optional[ExampleItem] = None
        self._current_source = ""
        self._last_tip: Optional[str] = None
        self._pool = QThreadPool.globalInstance()

        self._build_ui()
        self._load_examples()

    # ----------------------------------------------------------- интерфейс

    def _build_ui(self) -> None:
        root = QHBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(6)
        splitter.addWidget(self._build_left_panel())
        splitter.addWidget(self._build_right_panel())
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([290, 900])
        root.addWidget(splitter)

    def _build_left_panel(self) -> QWidget:
        panel = QFrame()
        panel.setProperty("panel", True)
        panel.setMinimumWidth(230)
        panel.setMaximumWidth(440)

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(6)

        layout.addWidget(section_label("ПОДКЛЮЧЕНИЕ"))

        self._host = line_edit("Хост, напр. localhost", "localhost")
        self._port = line_edit("Порт", "4398")
        self._port.setFixedWidth(88)
        layout.addLayout(row(self._host, self._port))

        self._token = line_edit("Токен (api_key)")
        layout.addWidget(self._token)

        self._device = line_edit("Имя ККМ, напр. Emu", "Emu")
        layout.addWidget(self._device)

        self._cashier = line_edit("Кассир, напр. Иванов А.И.")
        self._cashier_vatin = line_edit("ИНН кассира")
        self._cashier_vatin.setFixedWidth(140)
        layout.addLayout(row(self._cashier, self._cashier_vatin))

        self._document_id = line_edit("Id документа (DocId / taskId)")
        layout.addWidget(self._document_id)

        self._from = line_edit("С (yyyy-MM-dd)", (today() - timedelta(days=7)).strftime(DATE_FORMAT))
        self._to = line_edit("По (yyyy-MM-dd)", today().strftime(DATE_FORMAT))
        self._to.setFixedWidth(140)
        layout.addLayout(row(self._from, self._to))

        collection = section_label("КОЛЛЕКЦИЯ")
        collection.setContentsMargins(0, 8, 0, 0)
        layout.addWidget(collection)

        self._tree = QTreeWidget()
        self._tree.setHeaderHidden(True)
        self._tree.setIndentation(14)
        self._tree.setUniformRowHeights(True)
        self._tree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._tree.setItemDelegate(RequestDelegate(self._tree))
        self._tree.currentItemChanged.connect(self._on_example_selected)
        layout.addWidget(self._tree, 1)
        return panel

    def _build_right_panel(self) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        header = QFrame()
        header.setProperty("panel", True)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(12, 8, 12, 8)
        header_layout.setSpacing(10)

        self._method_pill = QLabel("")
        self._method_pill.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._method_pill.setMinimumWidth(58)
        self._method_pill.setVisible(False)
        header_layout.addWidget(self._method_pill)

        self._request_title = QLabel("Выберите запрос")
        title_font = QFont()
        title_font.setBold(True)
        self._request_title.setFont(title_font)
        header_layout.addWidget(self._request_title, 1)

        self._status = QLabel("")
        self._status.setMinimumWidth(120)
        self._status.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self._status.setFont(title_font)
        header_layout.addWidget(self._status)

        self._run = QPushButton("Выполнить")
        self._run.setProperty("accent", True)
        self._run.clicked.connect(self._on_run)
        header_layout.addWidget(self._run)

        self._cancel = QPushButton("Отменить")
        self._cancel.setEnabled(False)
        self._cancel.clicked.connect(self._on_cancel)
        header_layout.addWidget(self._cancel)

        layout.addWidget(header)

        panels = QSplitter(Qt.Orientation.Horizontal)
        panels.setHandleWidth(6)

        self._source = editor()
        self._source_highlighter = PythonHighlighter(self._source.document())
        self._source.viewport().setMouseTracking(True)
        self._source.viewport().installEventFilter(self)

        self._copy = QPushButton()
        self._copy.setIcon(theme.copy_icon())
        self._copy.setProperty("iconButton", True)
        self._copy.setToolTip("Копировать")
        self._copy.clicked.connect(self._on_copy)

        panels.addWidget(editor_panel("ЗАПРОС", self._source, self._copy))

        self._response = editor()
        self._response_highlighter = JsonHighlighter(self._response.document())
        panels.addWidget(editor_panel("ОТВЕТ", self._response))

        panels.setSizes([600, 600])
        layout.addWidget(panels, 1)
        return container

    # -------------------------------------------------------------- дерево

    def _load_examples(self) -> None:
        for node in build_tree():
            self._tree.addTopLevelItem(self._build_node(node))
        self._tree.expandAll()

    def _build_node(self, node: ExampleTreeNode) -> QTreeWidgetItem:
        if node.Item is not None:
            item = QTreeWidgetItem([node.Title])
            item.setData(0, ITEM_ROLE, node.Item)
            item.setData(0, METHOD_ROLE, node.Item.HttpMethod)
            item.setToolTip(0, f"{node.Item.HttpMethod} {node.Title}")
            return item

        folder = QTreeWidgetItem([node.Title])
        font = folder.font(0)
        font.setBold(True)
        folder.setFont(0, font)
        folder.setFlags(Qt.ItemFlag.ItemIsEnabled)
        for child in node.Children:
            folder.addChild(self._build_node(child))
        return folder

    def _on_example_selected(self, current: Optional[QTreeWidgetItem], _previous: object = None) -> None:
        if current is None:
            return
        example = current.data(0, ITEM_ROLE)
        if not isinstance(example, ExampleItem):
            return
        self._show_example(example)

    def _show_example(self, example: ExampleItem) -> None:
        self._selected = example
        self._current_source = example_source.read(example)
        self._request_title.setText(example.Title)
        self._method_pill.setVisible(True)
        self._method_pill.setText(example.HttpMethod)
        self._method_pill.setStyleSheet(
            f"background-color: {theme.METHOD_PILL_COLORS.get(example.HttpMethod, '#C4703A')};"
            "color: #FFFFFF; font-weight: bold; font-size: 12px;"
            "border-radius: 4px; padding: 3px 8px;"
        )
        self._copy.setToolTip("Копировать")
        self._source.setPlainText(self._current_source)
        self._response.setPlainText("")
        self._set_status("", theme.STATUS_IDLE)

    # -------------------------------------------------------------- запуск

    def _on_run(self) -> None:
        if self._selected is None:
            self._set_status("Выберите пример", theme.STATUS_IDLE)
            return

        self._read_connection()
        error = self._connection.try_read(self._selected.NeedDocumentId)
        if error:
            self._response.setPlainText(error)
            self._set_status("Проверьте подключение", theme.STATUS_IDLE)
            return

        self._run.setEnabled(False)
        self._cancel.setEnabled(True)
        self._set_status("Выполняется…", theme.STATUS_IDLE)

        ExampleRunner.apply_connection(self._selected.Instance, self._connection)
        worker = ExampleWorker(self._selected)
        worker.signals.finished.connect(self._on_finished)
        worker.signals.failed.connect(self._on_failed)
        self._pool.start(worker)

    def _on_finished(self, kkm: object) -> None:
        if isinstance(kkm, SkkmConnector):
            self._response.setPlainText(format_response(kkm))
            if kkm.ErrorCode == -3:
                self._set_status("Отменено", theme.STATUS_IDLE)
            else:
                self._set_status("OK" if kkm.Ok else "Error", theme.STATUS_OK if kkm.Ok else theme.STATUS_ERROR)
        self._finish_call()

    def _on_failed(self, message: str) -> None:
        self._response.setPlainText(message)
        self._set_status("Error", theme.STATUS_ERROR)
        self._finish_call()

    def _finish_call(self) -> None:
        self._run.setEnabled(True)
        self._cancel.setEnabled(False)

    def _on_cancel(self) -> None:
        ExampleRunner.Session.Cancel()

    def _on_copy(self) -> None:
        if not self._current_source:
            return
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self._current_source)
        self._copy.setToolTip("Скопировано")

    def _read_connection(self) -> None:
        self._connection.Host = self._host.text()
        self._connection.Port = int(self._port.text()) if self._port.text().strip().isdigit() else 0
        self._connection.Token = self._token.text()
        self._connection.Device = self._device.text()
        self._connection.Cashier = self._cashier.text()
        self._connection.CashierVatin = self._cashier_vatin.text()
        self._connection.DocumentId = self._document_id.text()
        self._connection.FromText = self._from.text()
        self._connection.ToText = self._to.text()

    def _set_status(self, text: str, color: str) -> None:
        self._status.setText(text)
        self._status.setStyleSheet(f"color: {color};")

    # ----------------------------------------------------------- подсказки

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:  # noqa: N802 - имя из Qt
        if watched is self._source.viewport() and isinstance(event, QMouseEvent):
            if event.type() == QEvent.Type.MouseMove:
                self._update_doc_tip(event)
            elif event.type() == QEvent.Type.Leave:
                QToolTip.hideText()
        return super().eventFilter(watched, event)

    def _update_doc_tip(self, event: QMouseEvent) -> None:
        cursor = self._source.cursorForPosition(event.position().toPoint())
        tip = doc_lookup.summary_at(self._current_source, cursor.position())
        if tip == self._last_tip:
            return
        self._last_tip = tip
        if tip is None:
            QToolTip.hideText()
            return
        QToolTip.showText(event.globalPosition().toPoint(), tip, self._source)

    def closeEvent(self, event: QEvent) -> None:  # noqa: N802 - имя из Qt
        ExampleRunner.Session.Dispose()
        super().closeEvent(event)  # type: ignore[arg-type]


# ---------------------------------------------------------------- виджеты

def section_label(text: str) -> QLabel:
    label = QLabel(text)
    label.setProperty("section", True)
    return label


def line_edit(placeholder: str, value: str = "") -> QLineEdit:
    field = QLineEdit()
    field.setPlaceholderText(placeholder)
    field.setText(value)
    return field


def row(*widgets: QWidget) -> QHBoxLayout:
    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(6)
    for widget in widgets:
        layout.addWidget(widget)
    return layout


def editor() -> QPlainTextEdit:
    widget = QPlainTextEdit()
    widget.setReadOnly(True)
    widget.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
    font = QFont("Cascadia Code")
    font.setStyleHint(QFont.StyleHint.Monospace)
    font.setPointSize(10)
    widget.setFont(font)
    return widget


def editor_panel(title: str, body: QWidget, *actions: QWidget) -> QWidget:
    panel = QFrame()
    panel.setProperty("editorPanel", True)
    layout = QVBoxLayout(panel)
    layout.setContentsMargins(1, 1, 1, 1)
    layout.setSpacing(0)

    header = QFrame()
    header.setProperty("header", True)
    header.setFixedHeight(36)
    header_layout = QHBoxLayout(header)
    header_layout.setContentsMargins(12, 0, 8, 0)
    header_layout.addWidget(section_label(title))
    header_layout.addStretch(1)
    for action in actions:
        header_layout.addWidget(action)

    layout.addWidget(header)
    layout.addWidget(body, 1)
    return panel
