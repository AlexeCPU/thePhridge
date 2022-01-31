# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets, QtCore
from mainwin import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    #functions



    #Buttons and crap goes here

    ui.Home.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(1))
    ui.Music.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(0))
    ui.CalcButt.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(2))

    MainWindow.show()
    sys.exit(app.exec())




