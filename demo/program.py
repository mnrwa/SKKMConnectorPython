"""Точка входа демо-приложения."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if __package__ in (None, ""):  # запуск как `python demo/program.py`
    sys.path.insert(0, str(ROOT))

if importlib.util.find_spec("rbsoftskkm") is None:  # коннектор не установлен — берём из исходников
    sys.path.insert(0, str(ROOT / "src"))

from PySide6.QtWidgets import QApplication  # noqa: E402 - импорт после настройки путей

from demo.app import apply_theme  # noqa: E402
from demo.main_window import MainWindow  # noqa: E402


def main() -> int:
    app = QApplication(sys.argv)
    apply_theme(app)

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
