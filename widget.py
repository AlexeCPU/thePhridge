# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5 import QtCore
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from formpython import Ui_Widget


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        _translate = QtCore.QCoreApplication.translate
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        calc = Ui_Widget()
        calc.setup()
        calc.calcOutput.setText(_translate("Widget", "TextLabel"))
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
