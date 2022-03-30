# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
from mainwin import Ui_MainWindow
from popup_window import PopupWindow

class Calc(QMainWindow):
	def init(self, ui):   
		print("Initiated Calculator Class")
		self.add_item_box = QMessageBox()
		self.add_item_box.setWindowTitle("Add New Item")
		self.add_item_box.setText("test text!")
		totalcalperday = 0
		ui.addItemToListButton.clicked.connect(lambda : self.handle_add_to_list(ui))
		ui.addHundCalsServ.clicked.connect(lambda: ui.calServ.setText(str(int(ui.calServ.text()) + 100)))
		ui.addTenCalsServ.clicked.connect(lambda: ui.calServ.setText(str(int(ui.calServ.text()) + 10)))
		ui.minusTenCalsServ.clicked.connect(lambda: ui.calServ.setText(str(int(ui.calServ.text()) - 10)))
		ui.minusHundCalsServ.clicked.connect(lambda: ui.calServ.setText(str(int(ui.calServ.text()) - 100)))
		ui.addFiveServ.clicked.connect(lambda: ui.serv.setText(str(int(ui.serv.text()) + 5)))
		ui.addOneServ.clicked.connect(lambda: ui.serv.setText(str(int(ui.serv.text()) + 1)))
		ui.minusOneServ.clicked.connect(lambda: ui.serv.setText(str(int(ui.serv.text()) - 1)))
		ui.minusFiveServ.clicked.connect(lambda: ui.serv.setText(str(int(ui.serv.text()) - 5)))
		ui.addItemButton.clicked.connect(lambda: self.add_item(ui))
		ui.servings.verticalScrollBar().valueChanged.connect(
            ui.foodName.verticalScrollBar().setValue)
		ui.servings.verticalScrollBar().valueChanged.connect(
            ui.calPerServing.verticalScrollBar().setValue)
		ui.servings.verticalScrollBar().valueChanged.connect(
            ui.calPerServing.verticalScrollBar().setValue)
		ui.consumebutton.clicked.connect(lambda:  self.consume(ui))

	def handle_add_to_list(self, ui):
		ui.stackedWidget.setCurrentIndex(3)
		ui.calServ.setText("0")
		ui.serv.setText("0")
		ui.lineEdit.setText("")

	def add_item(self, ui):
		ui.stackedWidget.setCurrentIndex(2)
		foodName = QListWidgetItem()
		foodName.setText(ui.lineEdit.text())
		ui.foodName.addItem(foodName)
		calPerServing = QListWidgetItem()
		calPerServing.setText(ui.calServ.text())
		ui.calPerServing.addItem(calPerServing)
		servings = QListWidgetItem()
		servings.setText(ui.serv.text())
		ui.servings.addItem(servings)

	def consume(self, ui):
		totalcalperday += str(selected)
		selected = ui.servings.currentRow()
		print(str(selected)
		print(totalcalperday))
		print("test")
	
		# print(totalcalperday)


# class EatenFood {
# 	def __init__(self, date, cals):
# 		self.date = date
# 		self.cals = cals
# }