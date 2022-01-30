# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

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
        self.SideBar.setStyleSheet(u"background: rgb(25, 25, 25);")
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
        self.Home.setFont(font)
        self.Home.setLayoutDirection(Qt.LeftToRight)
        self.Home.setAutoFillBackground(False)
        self.Home.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
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
        self.Home.setIconSize(QSize(25, 25))
        self.Home.setFlat(True)

        self.verticalLayout.addWidget(self.Home)

        self.Music = QPushButton(self.frame)
        self.Music.setObjectName(u"Music")
        self.Music.setMinimumSize(QSize(200, 40))
        self.Music.setFont(font)
        self.Music.setLayoutDirection(Qt.LeftToRight)
        self.Music.setAutoFillBackground(False)
        self.Music.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.Music.setIcon(icon)
        self.Music.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.Music)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(200, 45))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(200, 45))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(200, 45))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 900, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.SideBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(210, 200))
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setLineWidth(5)
        self.label_2.setPixmap(QPixmap(u"icons/phil.png"))
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
        self.MainBar.setStyleSheet(u"background:#141414;border-radius:2px")
        self.MainBar.setFrameShape(QFrame.StyledPanel)
        self.MainBar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.MainBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.MainBar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
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
        self.frame_2.setStyleSheet(u"background:red")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 391, 21))

        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.homepage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.MainBar)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Music, self.Home)
        QWidget.setTabOrder(self.Home, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Music.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Calorithmatic", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"aaaaaaaaaaaaaaaa", None))
    # retranslateUi

