from PySide2.QtWidgets import QWidget, QPlainTextEdit, QMainWindow
from PySide2.QtGui import QPainter

class PopupWindow(QMainWindow):
    def __init__(self):
        super(PopupWindow, self).__init__()
        foodName = QPlainTextEdit()
        foodName.setPlaceholderText("Food Name")
        self.addWidget(foodName)

    # def paintEvent(self, e):
    #     dc = QPainter(self)
    #     dc.drawLine(0, 0, 100, 100)
    #     dc.drawLine(100, 0, 0, 100)