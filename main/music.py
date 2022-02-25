# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
from mainwin import Ui_MainWindow
from popup_window import PopupWindow

class musicplayer(QMainWindow):
    def init(self, ui):
        print("initated")