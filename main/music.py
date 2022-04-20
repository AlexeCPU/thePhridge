# This Python file uses the following encoding: utf-8
import sys
import os
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow
from pydub import AudioSegment
from pydub.playback import play

class musicplayer(QMainWindow):
    def __init__(self, ui):
        print("__init__iated Music Class")
        
        # ui.eqViewer.load("/home/pi/thePhridge/main/index.html")

        mastermusiclist = os.listdir(path=r"/home/pi/thePhridge/main/audio")

        for val in mastermusiclist:
            if ".webp" in val:
                mastermusiclist.remove(val)
            else:
                ui.musicList.addItem(val)
        print(mastermusiclist)        

        ui.musicList.itemActivated.connect(lambda: self.onPress(ui.musicList.currentItem()))

        ui.pushButton_2.clicked.connect(lambda: self.playmusic(ui.musicList.currentItem()))

    def onPress(self, item):
        print(item.text())

    def playmusic(self,item):
        print(item.text())
        play(AudioSegment.from_wav('/home/pi/thePhridge/main/audio/'+item.text()))
