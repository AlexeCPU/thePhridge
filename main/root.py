# This Python file uses the following encoding: utf-8
import time, sys
from PySide2.QtWidgets import QMainWindow, QSplashScreen
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from PySide2 import QtWidgets, QtCore
from mainwin import Ui_MainWindow
from PySide2.QtWebEngineWidgets import *
from music import musicplayer
from calc import Calc
from settings import Settings
from visualizer import GLWidget

frame = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        self.glWidget = GLWidget()

        self.glWidgetArea = QtWidgets.QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QtWidgets.QSizePolicy.Ignored,
                QtWidgets.QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        # sliders
        x_slider = self.create_slider(self.glWidget.x_rotation_changed,
                                     self.glWidget.set_x_rot_speed)
        y_slider = self.create_slider(self.glWidget.y_rotation_changed,
                                     self.glWidget.set_y_rot_speed)
        z_slider = self.create_slider(self.glWidget.z_rotation_changed,
                                     self.glWidget.set_z_rot_speed)

        # set the layout
        central_layout = QtWidgets.QVBoxLayout()
        central_layout.addWidget(self.glWidgetArea)
        central_layout.addWidget(x_slider)
        central_layout.addWidget(y_slider)
        central_layout.addWidget(z_slider)
        central_widget.setLayout(central_layout)

        x_slider.setValue(1)
        y_slider.setValue(1)
        z_slider.setValue(0)

        self.setWindowTitle("Hello OpenGL")
        self.resize(400, 300)

    def create_slider(self, changedSignal, setterSlot):
        """Helper to create a slider."""
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 10)
        slider.setSingleStep(1)
        slider.setPageStep(5)
        slider.setTickInterval(2)
        slider.setTickPosition(QtWidgets.QSlider.TicksRight)

        slider.valueChanged.connect(setterSlot)
        changedSignal.connect(slider.setValue)

        return slider


def updateVoicePack(ui):
    settings.setValue("voice_pack",ui.voiceChoiceBox.currentText())
    settings.setValue("voice_pack_index",ui.voiceChoiceBox.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    geometry = app.desktop().availableGeometry()
    
    print("woaghshsdhahs")

    settings = Settings()
    settings.init("settings.json")

    MainWindow.setGeometry(geometry)
    # MainWindow.setWindowFlag(Qt.FramelessWindowHint)

    #functions

    if(len(sys.argv) < 2 or sys.argv[1] != "--no-splash"):
        frame = 1
        pixmap = QPixmap((f"/home/pi/the splash/splash000.jpg")).scaled(app.desktop().screenGeometry().width(), app.desktop().screenGeometry().height())
        splash=QSplashScreen(pixmap)
        splash.show()

        while frame != 420:
            milliseconds = int(round(time.time() * 1000))
            pixmap = QPixmap((f"/home/pi/the splash/splash{frame:03}.jpg")).scaled(app.desktop().screenGeometry().width(), app.desktop().screenGeometry().height())
            splash.setPixmap(pixmap)
            frame+=1
            time.sleep(max((1/60) - ((int(round(time.time() * 1000)) - milliseconds)/1000),0))
            app.processEvents()
        splash.hide()

    #Buttons and crap goes here

    ui.autoCloseSpinBox.setValue(int(settings.getValue("auto_off"))//60)
    ui.autoCloseSpinBox.valueChanged.connect(lambda: settings.setValue("auto_off",ui.autoCloseSpinBox.value()*60))

    ui.voiceChoiceBox.setCurrentIndex(settings.getValue("voice_pack_index"))
    ui.voiceSetButton.clicked.connect(lambda: updateVoicePack(ui))

    calc = Calc()
    calc.init(ui)

    music =  musicplayer()
    music.init(ui)

    ui.Home.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(1))
    ui.Music.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(0))
    ui.CalcButt.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(2))
    ui.Settings.clicked.connect(lambda : ui.stackedWidget.setCurrentIndex(4))

    MainWindow.show()
    res = app.exec_()
    MainWindow.glWidget.free_resources()
    sys.exit(res)




