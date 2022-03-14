import sys
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow
from PySide2.QtCharts import *


class TheHome(QMainWindow):
    def init(self, ui):
        print("Init Home Page")
        lay = ui.CalChartLayout #(QMainWindow)
        series = []

        # Create Chart and set General Chart setting
        chart = QtCharts.QChart()
        series = QtCharts.QLineSeries()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        # X Axis Settings
        axisX = QtCharts.QValueAxis()
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Y Axis Settings
        axisY = QtCharts.QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        chartview.setChart(chart)


