import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow
from PySide2.QtCharts import QtCharts
from random import randint
from settings import Settings
from calc import Calc
from pydub import AudioSegment
from pydub.playback import play
# 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

class TheHome(QMainWindow):

    def __init__(self, ui,totalcaltest):
        totalcalperday = totalcaltest
        print("Init Home Page")
        lay = ui.CalChartLayout #(QMainWindow)
        self.caldata = QtCharts.QLineSeries()

        calrawdata = [0]*7 # Populate calrawdata with 7 0's in a list

        # Store the raw data
        raw_data_store = Settings("calrawdata.json")
        raw_data_store.clear()

        for i in range(len(calrawdata)):
            raw_data_store.setValue(i, calrawdata[i]) # Store the value of calrawdata into the "calrawdata.json" file.

        TheHome.rebuildList(self, calrawdata,totalcalperday)
        
        # Creating QChart
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chart.addSeries(self.caldata)

        # Creating QChartView
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        lay.addWidget(self.chart_view)
        #This won't process clicks for some reason but throws no errors
        ui.CalChartRefresh.clicked.connect(lambda: TheHome.rebuildList(self))
        
    def rebuildList(self, theList,cal):
        print(cal)
        for i in range(len(theList)):
            #QPointF is i, which is the part it is in, process this based on list placement, and replace randint with the list entry value
            self.caldata << QPointF(i, theList[i])
        if cal < 1000:
            play(AudioSegment.from_wav("/home/pi/thePhridge/main/quote/"+"PHIL_"+'underate.wav'))
        elif cal > 2000:
            play(AudioSegment.from_wav('overate.wav'))
        else:
            pplay(AudioSegment.from_wav('goodate.wav'))

        # self.chart_view.setStyleSheet(u"QLegend {\n"
        # "	display: none;\n"
        # "	background-color: rgb(255,0,0);\n"
        # "}\n")

    # def populateChart():
    #     series.append(0, 6)
    #     series.append(1, 4)
    #     series.append(2, 5)
    #     series.append(3, 10)
    #     series.append(4, 16)
    #     series.append(5, 2)

    #     self.chart_view.chart().removeAllSeries()
    #     self.chart_view.chart().addSeries(series)





