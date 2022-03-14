# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:#121212")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.SideBar = QFrame(self.centralwidget)
        self.SideBar.setObjectName(u"SideBar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
        self.SideBar.setMinimumSize(QSize(0, 0))
        self.SideBar.setMaximumSize(QSize(300, 16777215))
        self.SideBar.setStyleSheet(u"background: rgb(35, 35, 35);")
        self.SideBar.setFrameShape(QFrame.StyledPanel)
        self.SideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SideBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.SideBar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Home = QPushButton(self.frame)
        self.Home.setObjectName(u"Home")
        self.Home.setMinimumSize(QSize(200, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Home.setFont(font)
        self.Home.setLayoutDirection(Qt.LeftToRight)
        self.Home.setAutoFillBackground(False)
        self.Home.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid #0050B5;\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QSize(20, 20))
        self.Home.setFlat(False)

        self.verticalLayout.addWidget(self.Home)

        self.Music = QPushButton(self.frame)
        self.Music.setObjectName(u"Music")
        self.Music.setMinimumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamily(u"Noto Mono")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.Music.setFont(font1)
        self.Music.setLayoutDirection(Qt.LeftToRight)
        self.Music.setAutoFillBackground(False)
        self.Music.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid #0050B5;\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Music.setIcon(icon1)
        self.Music.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.Music)

        self.CalcButt = QPushButton(self.frame)
        self.CalcButt.setObjectName(u"CalcButt")
        self.CalcButt.setMinimumSize(QSize(200, 45))
        font2 = QFont()
        font2.setFamily(u"Monospace")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.CalcButt.setFont(font2)
        self.CalcButt.setLayoutDirection(Qt.LeftToRight)
        self.CalcButt.setAutoFillBackground(False)
        self.CalcButt.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid #0050B5;\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CalcButt.setIcon(icon2)
        self.CalcButt.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.CalcButt)

        self.Settings = QPushButton(self.frame)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMinimumSize(QSize(200, 45))
        self.Settings.setFont(font)
        self.Settings.setLayoutDirection(Qt.LeftToRight)
        self.Settings.setAutoFillBackground(False)
        self.Settings.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid #0050B5;\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        iconThemeName = u"settings.svg"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.Settings.setIcon(icon3)

        self.verticalLayout.addWidget(self.Settings)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 900, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.SideBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(210, 240))
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setLineWidth(5)
        self.label_2.setPixmap(QPixmap(u"icons/Phil.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.SideBar)

        self.MainBar = QFrame(self.centralwidget)
        self.MainBar.setObjectName(u"MainBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBar.sizePolicy().hasHeightForWidth())
        self.MainBar.setSizePolicy(sizePolicy1)
        self.MainBar.setStyleSheet(u"background:rgb(50, 50, 50);border-radius:2px")
        self.MainBar.setFrameShape(QFrame.StyledPanel)
        self.MainBar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.MainBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.MainBar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.musicpage = QWidget()
        self.musicpage.setObjectName(u"musicpage")
        self.verticalLayoutWidget = QWidget(self.musicpage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 801, 571))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.eqViewer = QWebEngineView(self.verticalLayoutWidget)
        self.eqViewer.setObjectName(u"eqViewer")

        self.horizontalLayout_2.addWidget(self.eqViewer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalSpacer_8 = QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_3.addItem(self.verticalSpacer_8)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(150, 150))
        self.pushButton_2.setMaximumSize(QSize(150, 150))
        self.pushButton_2.setStyleSheet(u"border-radius:49%;background-color:rgb(40,40,40)")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.openYTDL = QPushButton(self.verticalLayoutWidget)
        self.openYTDL.setObjectName(u"openYTDL")
        self.openYTDL.setStyleSheet(u"color:white")

        self.horizontalLayout_4.addWidget(self.openYTDL)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_4.addItem(self.verticalSpacer_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.musicpage)
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.layoutWidget = QWidget(self.homepage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 391, 571))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 391, 21))
        self.label.setStyleSheet(u"color:white")

        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.homepage)
        self.calcpage = QWidget()
        self.calcpage.setObjectName(u"calcpage")
        self.calcpage.setStyleSheet(u"")
        self.frame_5 = QFrame(self.calcpage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 781, 571))
        self.frame_5.setStyleSheet(u"QFrame{background:#373737;\n"
"border-radius:5px;\n"
"border-left:3px solid #0050B5;}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 631, 551))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"Background-color:rgb(40, 40, 40);border:none;color:white")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(75, 16777215))
        font3 = QFont()
        font3.setPointSize(8)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"Background-color:rgb(40, 40, 40);border:none;color:white")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"Background-color:rgb(40, 40, 40);border:none;color:white")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.nutritionTable = QHBoxLayout()
        self.nutritionTable.setObjectName(u"nutritionTable")
        self.foodName = QListWidget(self.verticalLayoutWidget_2)
        self.foodName.setObjectName(u"foodName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.foodName.sizePolicy().hasHeightForWidth())
        self.foodName.setSizePolicy(sizePolicy3)
        self.foodName.setStyleSheet(u"QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"	background-color:rgb(38, 38, 38);\n"
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
"            subcontrol-"
                        "origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.foodName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.foodName.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.nutritionTable.addWidget(self.foodName)

        self.calPerServing = QListWidget(self.verticalLayoutWidget_2)
        self.calPerServing.setObjectName(u"calPerServing")
        self.calPerServing.setMaximumSize(QSize(75, 16777215))
        self.calPerServing.setStyleSheet(u"QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"	background-color:rgb(38, 38, 38);\n"
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
"            subcontrol-"
                        "origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.calPerServing.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.nutritionTable.addWidget(self.calPerServing)

        self.servings = QListWidget(self.verticalLayoutWidget_2)
        self.servings.setObjectName(u"servings")
        self.servings.setMaximumSize(QSize(50, 16777215))
        self.servings.setStyleSheet(u"QListWidget{Background-color:rgb(40, 40, 40);border:none}\n"
"\n"
"QListWidget::item {\n"
"	background-color:rgb(38, 38, 38);\n"
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
"            subcontrol-"
                        "origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.servings.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.nutritionTable.addWidget(self.servings)


        self.verticalLayout_7.addLayout(self.nutritionTable)

        self.addItemToListButton = QPushButton(self.frame_5)
        self.addItemToListButton.setObjectName(u"addItemToListButton")
        self.addItemToListButton.setGeometry(QRect(650, 10, 121, 91))
        self.addItemToListButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(40, 40, 40);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-right: 3px solid rgb(25, 25, 25);\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-right: 3px solid #0050B5;\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.calcpage)
        self.addItemPage = QWidget()
        self.addItemPage.setObjectName(u"addItemPage")
        self.verticalLayoutWidget_3 = QWidget(self.addItemPage)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 791, 571))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.calperserv = QLabel(self.verticalLayoutWidget_3)
        self.calperserv.setObjectName(u"calperserv")
        self.calperserv.setStyleSheet(u"color:white;")

        self.horizontalLayout_5.addWidget(self.calperserv)

        self.minusHundCalsServ = QPushButton(self.verticalLayoutWidget_3)
        self.minusHundCalsServ.setObjectName(u"minusHundCalsServ")
        self.minusHundCalsServ.setMaximumSize(QSize(50, 16777215))
        self.minusHundCalsServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_5.addWidget(self.minusHundCalsServ)

        self.minusTenCalsServ = QPushButton(self.verticalLayoutWidget_3)
        self.minusTenCalsServ.setObjectName(u"minusTenCalsServ")
        self.minusTenCalsServ.setMaximumSize(QSize(50, 16777215))
        self.minusTenCalsServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_5.addWidget(self.minusTenCalsServ)

        self.calServ = QLineEdit(self.verticalLayoutWidget_3)
        self.calServ.setObjectName(u"calServ")
        self.calServ.setMaximumSize(QSize(50, 16777215))
        self.calServ.setStyleSheet(u"color:white;")
        self.calServ.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.calServ)

        self.addTenCalsServ = QPushButton(self.verticalLayoutWidget_3)
        self.addTenCalsServ.setObjectName(u"addTenCalsServ")
        self.addTenCalsServ.setMaximumSize(QSize(50, 16777215))
        self.addTenCalsServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_5.addWidget(self.addTenCalsServ)

        self.addHundCalsServ = QPushButton(self.verticalLayoutWidget_3)
        self.addHundCalsServ.setObjectName(u"addHundCalsServ")
        self.addHundCalsServ.setMaximumSize(QSize(50, 16777215))
        self.addHundCalsServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_5.addWidget(self.addHundCalsServ)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.servtex = QLabel(self.verticalLayoutWidget_3)
        self.servtex.setObjectName(u"servtex")
        self.servtex.setStyleSheet(u"color:white;")

        self.horizontalLayout_8.addWidget(self.servtex)

        self.minusFiveServ = QPushButton(self.verticalLayoutWidget_3)
        self.minusFiveServ.setObjectName(u"minusFiveServ")
        self.minusFiveServ.setMaximumSize(QSize(50, 16777215))
        self.minusFiveServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_8.addWidget(self.minusFiveServ)

        self.minusOneServ = QPushButton(self.verticalLayoutWidget_3)
        self.minusOneServ.setObjectName(u"minusOneServ")
        self.minusOneServ.setMaximumSize(QSize(50, 16777215))
        self.minusOneServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_8.addWidget(self.minusOneServ)

        self.serv = QLineEdit(self.verticalLayoutWidget_3)
        self.serv.setObjectName(u"serv")
        self.serv.setMaximumSize(QSize(50, 16777215))
        self.serv.setStyleSheet(u"color:white;")
        self.serv.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.serv)

        self.addOneServ = QPushButton(self.verticalLayoutWidget_3)
        self.addOneServ.setObjectName(u"addOneServ")
        self.addOneServ.setMaximumSize(QSize(50, 16777215))
        self.addOneServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_8.addWidget(self.addOneServ)

        self.addFiveServ = QPushButton(self.verticalLayoutWidget_3)
        self.addFiveServ.setObjectName(u"addFiveServ")
        self.addFiveServ.setMaximumSize(QSize(50, 16777215))
        self.addFiveServ.setStyleSheet(u"color:white;")

        self.horizontalLayout_8.addWidget(self.addFiveServ)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.addItemButton = QPushButton(self.verticalLayoutWidget_3)
        self.addItemButton.setObjectName(u"addItemButton")
        self.addItemButton.setStyleSheet(u"color:white;")

        self.verticalLayout_4.addWidget(self.addItemButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.addItemPage)
        self.settingspage = QWidget()
        self.settingspage.setObjectName(u"settingspage")
        self.frame_4 = QFrame(self.settingspage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 401, 241))
        self.frame_4.setStyleSheet(u"QFrame{background-color:#373737;\n"
"border-left:3px solid #0050B5;\n"
"border-radius:2px}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.autoCloseSpinBox = QSpinBox(self.frame_4)
        self.autoCloseSpinBox.setObjectName(u"autoCloseSpinBox")
        self.autoCloseSpinBox.setGeometry(QRect(10, 50, 53, 28))
        self.autoCloseSpinBox.setStyleSheet(u"	background-color: rgb(40, 40, 40);\n"
"	color:white;\n"
"	border-radius:10px")
        self.autoCloseSpinBox.setMinimum(1)
        self.autoCloseSpinBox.setMaximum(5)
        self.autoCloseSpinBox.setValue(1)
        self.voiceChoiceBox = QComboBox(self.frame_4)
        self.voiceChoiceBox.addItem("")
        self.voiceChoiceBox.addItem("")
        self.voiceChoiceBox.setObjectName(u"voiceChoiceBox")
        self.voiceChoiceBox.setGeometry(QRect(10, 10, 151, 27))
        self.voiceChoiceBox.setStyleSheet(u"	background-color: rgb(40, 40, 40);\n"
"	color:white;\n"
"	border-radius:10px")
        self.voiceSetButton = QPushButton(self.frame_4)
        self.voiceSetButton.setObjectName(u"voiceSetButton")
        self.voiceSetButton.setGeometry(QRect(170, 10, 51, 27))
        self.voiceSetButton.setStyleSheet(u"	background-color: rgb(40, 40, 40);\n"
"	color:white;\n"
"	border-radius:10px")
        self.stackedWidget.addWidget(self.settingspage)
        self.youtubedlpage = QWidget()
        self.youtubedlpage.setObjectName(u"youtubedlpage")
        self.frame_6 = QFrame(self.youtubedlpage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 601, 311))
        self.frame_6.setStyleSheet(u"QFrame{background-color:#373737;\n"
"border-left:3px solid #0050B5;\n"
"border-radius:2px}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.ytdlinput = QLineEdit(self.frame_6)
        self.ytdlinput.setObjectName(u"ytdlinput")
        self.ytdlinput.setGeometry(QRect(60, 20, 261, 27))
        self.ytdlinput.setStyleSheet(u"	background-color: rgb(40, 40, 40);\n"
"	color:white;\n"
"	border-radius:10px")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 20, 100, 27))
        self.pushButton.setStyleSheet(u"	background-color: rgb(40, 40, 40);\n"
"	color:white;\n"
"	border-radius:10px")
        self.stackedWidget.addWidget(self.youtubedlpage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.MainBar)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Music, self.Home)
        QWidget.setTabOrder(self.Home, self.CalcButt)
        QWidget.setTabOrder(self.CalcButt, self.Settings)

        self.retranslateUi(MainWindow)
        self.Home.clicked.connect(self.stackedWidget.update)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Music.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.CalcButt.setText(QCoreApplication.translate("MainWindow", u"Calorithmatic", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText("")
        self.pushButton_2.setText("")
        self.openYTDL.setText(QCoreApplication.translate("MainWindow", u"OpenYTDL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome home!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Food Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cal/Serving", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Servings", None))
        self.addItemToListButton.setText(QCoreApplication.translate("MainWindow", u"Add to List", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Food Name", None))
        self.calperserv.setText(QCoreApplication.translate("MainWindow", u"Cals / Serving", None))
        self.minusHundCalsServ.setText(QCoreApplication.translate("MainWindow", u"-100", None))
        self.minusTenCalsServ.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.addTenCalsServ.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.addHundCalsServ.setText(QCoreApplication.translate("MainWindow", u"+100", None))
        self.servtex.setText(QCoreApplication.translate("MainWindow", u"Servings", None))
        self.minusFiveServ.setText(QCoreApplication.translate("MainWindow", u"-5", None))
        self.minusOneServ.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.addOneServ.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.addFiveServ.setText(QCoreApplication.translate("MainWindow", u"+5", None))
        self.addItemButton.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.voiceChoiceBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Phil", None))
        self.voiceChoiceBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sans", None))

        self.voiceSetButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

