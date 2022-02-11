# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets, QtCore
from mainwin import Ui_MainWindow



class Calc(QMainWindow):
	def init(self, ui):    
		ui.calcText.setText("")
		ui.calcBackButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text()[0 : -1]))
		ui.calcAddButton.clicked.connect(lambda : ui.calcText.setText(""))
		ui.calcOneButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "1"))
		ui.calcTwoButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "2"))
		ui.calcThreeButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "3"))
		ui.calcFourButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "4"))
		ui.calcFiveButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "5"))
		ui.calcSixButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "6"))
		ui.calcSevenButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "7"))
		ui.calcEightButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "8"))
		ui.calcNineButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "9"))
		ui.calcZeroButton.clicked.connect(lambda : ui.calcText.setText(ui.calcText.text() + "0"))
