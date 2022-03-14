import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow
from PySide2.QtCharts import QtCharts


class TheHome(QMainWindow):
    def init(self, ui):
        print("Init Home Page")
        lay = ui.CalChartLayout #(QMainWindow)
        # Creating QChart
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        # Creating QChartView
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        lay.addWidget(self.chart_view)

        # Setting X-axis
        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)
        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)




