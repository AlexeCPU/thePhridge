# ydl1.py
from __future__ import unicode_literals
import sys
from PySide2.QtWidgets import QMainWindow, QLabel, QListWidgetItem, QMessageBox
from PySide2.QtCore import QRect
import PySide2.QtWebEngineCore
from mainwin import Ui_MainWindow
from popup_window import PopupWindow
from youtube_dl import YoutubeDL
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True','writethumbnail':'True',  'outtmpl': "/home/pi/thePhridge/main/audio/"+Ui_MainWindow().ytdltitle.text()+".%(ext)s"}



# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=dP15zlyra3c'])

class ytdlDown(QMainWindow):
    def __init__(self, ui):

        print("inait ytdl")
        ui.ytdsearch.clicked.connect(lambda : ytdlDown.search(ui.ytdlinput.text()))
        print(ui.ytdlinput.text())


    def search(arg):
        with YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                get(arg) 
            except:
                video = ydl.extract_info(f"ytsearch:{arg}", download=True)['entries'][0]
            else:
                video = ydl.extract_info(arg, download=True)

        return video