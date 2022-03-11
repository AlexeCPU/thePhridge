# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/thePhridge/main/main.ui',
# licensing of '/home/pi/Documents/thePhridge/main/main.ui' applies.
#
# Created: Tue Mar  8 11:31:24 2022
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:#121212")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
        self.SideBar.setMinimumSize(QtCore.QSize(0, 0))
        self.SideBar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.SideBar.setStyleSheet("background: rgb(35, 35, 35);")
        self.SideBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.SideBar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Home = QtWidgets.QPushButton(self.frame)
        self.Home.setMinimumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.Home.setFont(font)
        self.Home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Home.setAutoFillBackground(False)
        self.Home.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(154, 154, 149);\n"
"    border: none;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #0050B5;\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QtCore.QSize(20, 20))
        self.Home.setFlat(False)
        self.Home.setObjectName("Home")
        self.verticalLayout.addWidget(self.Home)
        self.Music = QtWidgets.QPushButton(self.frame)
        self.Music.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.Music.setFont(font)
        self.Music.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Music.setAutoFillBackground(False)
        self.Music.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(154, 154, 149);\n"
"    border: none;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #0050B5;\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Music.setIcon(icon1)
        self.Music.setIconSize(QtCore.QSize(20, 20))
        self.Music.setObjectName("Music")
        self.verticalLayout.addWidget(self.Music)
        self.CalcButt = QtWidgets.QPushButton(self.frame)
        self.CalcButt.setMinimumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.CalcButt.setFont(font)
        self.CalcButt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CalcButt.setAutoFillBackground(False)
        self.CalcButt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(154, 154, 149);\n"
"    border: none;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #0050B5;\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/sliders.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalcButt.setIcon(icon2)
        self.CalcButt.setIconSize(QtCore.QSize(20, 20))
        self.CalcButt.setObjectName("CalcButt")
        self.verticalLayout.addWidget(self.CalcButt)
        self.Settings = QtWidgets.QPushButton(self.frame)
        self.Settings.setMinimumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.Settings.setFont(font)
        self.Settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Settings.setAutoFillBackground(False)
        self.Settings.setStyleSheet("QPushButton {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(154, 154, 149);\n"
"    border: none;\n"
"    border-left: 3px solid rgb(25, 25, 25);\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-left: 3px solid #0050B5;\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Settings.setIcon(icon3)
        self.Settings.setObjectName("Settings")
        self.verticalLayout.addWidget(self.Settings)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 900, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.SideBar)
        self.label_2.setMaximumSize(QtCore.QSize(210, 240))
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(5)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/Phil.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.SideBar)
        self.MainBar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBar.sizePolicy().hasHeightForWidth())
        self.MainBar.setSizePolicy(sizePolicy)
        self.MainBar.setStyleSheet("background:rgb(50, 50, 50);border-radius:2px")
        self.MainBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBar.setObjectName("MainBar")
        self.gridLayout = QtWidgets.QGridLayout(self.MainBar)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.MainBar)
        self.stackedWidget.setObjectName("stackedWidget")
        self.musicpage = QtWidgets.QWidget()
        self.musicpage.setObjectName("musicpage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.musicpage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QWebEnginePage(self.verticalLayoutWidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setStyleSheet("border-radius:49%;background-color:rgb(40,40,40)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("color:white")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.musicpage)
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.layoutWidget = QtWidgets.QWidget(self.homepage)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.homepage)
        self.calcpage = QtWidgets.QWidget()
        self.calcpage.setStyleSheet("")
        self.calcpage.setObjectName("calcpage")
        self.frame_5 = QtWidgets.QFrame(self.calcpage)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 781, 571))
        self.frame_5.setStyleSheet("QFrame{background:#373737;\n"
"border-radius:5px;\n"
"border-left:3px solid #0050B5;}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 631, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setStyleSheet("Background-color:rgb(40, 40, 40);border:none;color:white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("Background-color:rgb(40, 40, 40);border:none;color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Background-color:rgb(40, 40, 40);border:none;color:white")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.nutritionTable = QtWidgets.QHBoxLayout()
        self.nutritionTable.setObjectName("nutritionTable")
        self.foodName = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodName.sizePolicy().hasHeightForWidth())
        self.foodName.setSizePolicy(sizePolicy)
        self.foodName.setStyleSheet("QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"    background-color:rgb(38, 38, 38);\n"
"color:white;\n"
"margin-bottom:1;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #555555;\n"
"}\n"
"\n"
"        QScrollBar:vertical {              \n"
"            border: none;\n"
"            background:white;\n"
"            width:3px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.foodName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.foodName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.foodName.setObjectName("foodName")
        self.nutritionTable.addWidget(self.foodName)
        self.calPerServing = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.calPerServing.setMaximumSize(QtCore.QSize(75, 16777215))
        self.calPerServing.setStyleSheet("QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"    background-color:rgb(38, 38, 38);\n"
"color:white;\n"
"margin-bottom:1;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #555555;\n"
"}\n"
"\n"
"        QScrollBar:vertical {              \n"
"            border: none;\n"
"            background:white;\n"
"            width:3px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.calPerServing.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.calPerServing.setObjectName("calPerServing")
        self.nutritionTable.addWidget(self.calPerServing)
        self.servings = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.servings.setMaximumSize(QtCore.QSize(50, 16777215))
        self.servings.setStyleSheet("QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"    background-color:rgb(38, 38, 38);\n"
"color:white;\n"
"margin-bottom:1;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 2px solid grey;\n"
"    background: #555555;\n"
"}\n"
"\n"
"        QScrollBar:vertical {              \n"
"            border: none;\n"
"            background:white;\n"
"            width:3px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.servings.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.servings.setObjectName("servings")
        self.nutritionTable.addWidget(self.servings)
        self.verticalLayout_7.addLayout(self.nutritionTable)
        self.addItemToListButton = QtWidgets.QPushButton(self.frame_5)
        self.addItemToListButton.setGeometry(QtCore.QRect(650, 10, 121, 91))
        self.addItemToListButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(40, 40, 40);\n"
"    color: rgb(154, 154, 149);\n"
"    border: none;\n"
"    border-right: 3px solid rgb(25, 25, 25);\n"
"    text-align: center;\n"
"    padding-left: 10px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-right: 3px solid #0050B5;\n"
"    background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(25, 25, 25);\n"
"}\n"
"\n"
"")
        self.addItemToListButton.setObjectName("addItemToListButton")
        self.stackedWidget.addWidget(self.calcpage)
        self.addItemPage = QtWidgets.QWidget()
        self.addItemPage.setObjectName("addItemPage")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.addItemPage)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.calperserv = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.calperserv.setStyleSheet("color:white;")
        self.calperserv.setObjectName("calperserv")
        self.horizontalLayout_5.addWidget(self.calperserv)
        self.minusHundCalsServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.minusHundCalsServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minusHundCalsServ.setStyleSheet("color:white;")
        self.minusHundCalsServ.setObjectName("minusHundCalsServ")
        self.horizontalLayout_5.addWidget(self.minusHundCalsServ)
        self.minusTenCalsServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.minusTenCalsServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minusTenCalsServ.setStyleSheet("color:white;")
        self.minusTenCalsServ.setObjectName("minusTenCalsServ")
        self.horizontalLayout_5.addWidget(self.minusTenCalsServ)
        self.calServ = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.calServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.calServ.setStyleSheet("color:white;")
        self.calServ.setReadOnly(True)
        self.calServ.setObjectName("calServ")
        self.horizontalLayout_5.addWidget(self.calServ)
        self.addTenCalsServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addTenCalsServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addTenCalsServ.setStyleSheet("color:white;")
        self.addTenCalsServ.setObjectName("addTenCalsServ")
        self.horizontalLayout_5.addWidget(self.addTenCalsServ)
        self.addHundCalsServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addHundCalsServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addHundCalsServ.setStyleSheet("color:white;")
        self.addHundCalsServ.setObjectName("addHundCalsServ")
        self.horizontalLayout_5.addWidget(self.addHundCalsServ)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.servtex = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.servtex.setStyleSheet("color:white;")
        self.servtex.setObjectName("servtex")
        self.horizontalLayout_8.addWidget(self.servtex)
        self.minusFiveServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.minusFiveServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minusFiveServ.setStyleSheet("color:white;")
        self.minusFiveServ.setObjectName("minusFiveServ")
        self.horizontalLayout_8.addWidget(self.minusFiveServ)
        self.minusOneServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.minusOneServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minusOneServ.setStyleSheet("color:white;")
        self.minusOneServ.setObjectName("minusOneServ")
        self.horizontalLayout_8.addWidget(self.minusOneServ)
        self.serv = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.serv.setMaximumSize(QtCore.QSize(50, 16777215))
        self.serv.setStyleSheet("color:white;")
        self.serv.setReadOnly(True)
        self.serv.setObjectName("serv")
        self.horizontalLayout_8.addWidget(self.serv)
        self.addOneServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addOneServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addOneServ.setStyleSheet("color:white;")
        self.addOneServ.setObjectName("addOneServ")
        self.horizontalLayout_8.addWidget(self.addOneServ)
        self.addFiveServ = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addFiveServ.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addFiveServ.setStyleSheet("color:white;")
        self.addFiveServ.setObjectName("addFiveServ")
        self.horizontalLayout_8.addWidget(self.addFiveServ)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.addItemButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addItemButton.setStyleSheet("color:white;")
        self.addItemButton.setObjectName("addItemButton")
        self.verticalLayout_4.addWidget(self.addItemButton)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.stackedWidget.addWidget(self.addItemPage)
        self.settingspage = QtWidgets.QWidget()
        self.settingspage.setObjectName("settingspage")
        self.frame_4 = QtWidgets.QFrame(self.settingspage)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 401, 241))
        self.frame_4.setStyleSheet("QFrame{background-color:#373737;\n"
"border-left:3px solid #0050B5;\n"
"border-radius:2px}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.autoCloseSpinBox = QtWidgets.QSpinBox(self.frame_4)
        self.autoCloseSpinBox.setGeometry(QtCore.QRect(10, 50, 53, 28))
        self.autoCloseSpinBox.setStyleSheet("    background-color: rgb(40, 40, 40);\n"
"    color:white;\n"
"    border-radius:10px")
        self.autoCloseSpinBox.setMinimum(1)
        self.autoCloseSpinBox.setMaximum(5)
        self.autoCloseSpinBox.setProperty("value", 1)
        self.autoCloseSpinBox.setObjectName("autoCloseSpinBox")
        self.voiceChoiceBox = QtWidgets.QComboBox(self.frame_4)
        self.voiceChoiceBox.setGeometry(QtCore.QRect(10, 10, 151, 27))
        self.voiceChoiceBox.setStyleSheet("    background-color: rgb(40, 40, 40);\n"
"    color:white;\n"
"    border-radius:10px")
        self.voiceChoiceBox.setObjectName("voiceChoiceBox")
        self.voiceChoiceBox.addItem("")
        self.voiceChoiceBox.addItem("")
        self.voiceSetButton = QtWidgets.QPushButton(self.frame_4)
        self.voiceSetButton.setGeometry(QtCore.QRect(170, 10, 51, 27))
        self.voiceSetButton.setStyleSheet("    background-color: rgb(40, 40, 40);\n"
"    color:white;\n"
"    border-radius:10px")
        self.voiceSetButton.setObjectName("voiceSetButton")
        self.stackedWidget.addWidget(self.settingspage)
        self.youtubedlpage = QtWidgets.QWidget()
        self.youtubedlpage.setObjectName("youtubedlpage")
        self.frame_6 = QtWidgets.QFrame(self.youtubedlpage)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 601, 311))
        self.frame_6.setStyleSheet("QFrame{background-color:#373737;\n"
"border-left:3px solid #0050B5;\n"
"border-radius:2px}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.ytdlinput = QtWidgets.QLineEdit(self.frame_6)
        self.ytdlinput.setGeometry(QtCore.QRect(60, 20, 261, 27))
        self.ytdlinput.setStyleSheet("    background-color: rgb(40, 40, 40);\n"
"    color:white;\n"
"    border-radius:10px")
        self.ytdlinput.setObjectName("ytdlinput")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 100, 27))
        self.pushButton.setStyleSheet("    background-color: rgb(40, 40, 40);\n"
"    color:white;\n"
"    border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.youtubedlpage)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.MainBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.Home, QtCore.SIGNAL("clicked()"), self.stackedWidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Music, self.Home)
        MainWindow.setTabOrder(self.Home, self.CalcButt)
        MainWindow.setTabOrder(self.CalcButt, self.Settings)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.Home.setText(QtWidgets.QApplication.translate("MainWindow", "Home", None, -1))
        self.Music.setText(QtWidgets.QApplication.translate("MainWindow", "Music", None, -1))
        self.CalcButt.setText(QtWidgets.QApplication.translate("MainWindow", "Calorithmatic", None, -1))
        self.Settings.setText(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Youtube Downloader", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Welcome home!", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Food Name", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Cal/Serving", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Servings", None, -1))
        self.addItemToListButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add to List", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Food Name", None, -1))
        self.calperserv.setText(QtWidgets.QApplication.translate("MainWindow", "Cals / Serving", None, -1))
        self.minusHundCalsServ.setText(QtWidgets.QApplication.translate("MainWindow", "-100", None, -1))
        self.minusTenCalsServ.setText(QtWidgets.QApplication.translate("MainWindow", "-10", None, -1))
        self.addTenCalsServ.setText(QtWidgets.QApplication.translate("MainWindow", "+10", None, -1))
        self.addHundCalsServ.setText(QtWidgets.QApplication.translate("MainWindow", "+100", None, -1))
        self.servtex.setText(QtWidgets.QApplication.translate("MainWindow", "Servings", None, -1))
        self.minusFiveServ.setText(QtWidgets.QApplication.translate("MainWindow", "-5", None, -1))
        self.minusOneServ.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.addOneServ.setText(QtWidgets.QApplication.translate("MainWindow", "+1", None, -1))
        self.addFiveServ.setText(QtWidgets.QApplication.translate("MainWindow", "+5", None, -1))
        self.addItemButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add Item", None, -1))
        self.voiceChoiceBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Phil", None, -1))
        self.voiceChoiceBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Sans", None, -1))
        self.voiceSetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))

from PySide2.QtWebEngineWidgets import QWebEnginePage
