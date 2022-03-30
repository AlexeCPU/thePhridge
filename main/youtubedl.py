# ydl1.py
from __future__ import unicode_literals
import youtube_dl
import sys
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=dP15zlyra3c'])

class ytdlDown(QMainWindow):
    def init(self, ui):
        print("inait ytdl")
        ui.ytdsearch.clicked.connect(lambda: print(ui.ytdlinput.text()))
        print(ui.ytdlinput.text())