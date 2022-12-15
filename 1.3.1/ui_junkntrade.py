# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'junkntradeazKMLx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sqlite3
from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc
import logos_rc

# create database
db = sqlite3.connect('wasteManagement.db')
cursor = db.cursor()

# creating member table
cursor.execute("CREATE TABLE IF NOT EXISTS member \
        (memberID INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT, \
               contactNumber TEXT, emailAddress TEXT, username TEXT NOT NULL, password TEXT NOT NULL, \
               rewardPoints INT)")

# creating shops table
cursor.execute("CREATE TABLE IF NOT EXISTS shops (shopID INTEGER PRIMARY KEY AUTOINCREMENT, shopAddress TEXT NOT NULL,\
                shopBranch TEXT NOT NULL)")

# creating junks table
cursor.execute("CREATE TABLE IF NOT EXISTS junks (junkID INTEGER PRIMARY KEY AUTOINCREMENT, junkName TEXT, junkType TEXT,\
                description TEXT)")

# creating rewards table
cursor.execute("CREATE TABLE IF NOT EXISTS rewards (rewardID INTEGER PRIMARY KEY AUTOINCREMENT, rewardName TEXT UNIQUE, rewardAmount INT)")

# creating records table
cursor.execute("CREATE TABLE IF NOT EXISTS records (recordID INTEGER PRIMARY KEY AUTOINCREMENT, memberID INT NOT NULL, \
           rewardName TEXT NOT NULL, rewardAmount INT NOT NULL, date TEXT,\
           FOREIGN KEY(memberID) REFERENCES member(memberID),\
           FOREIGN KEY(rewardName) REFERENCES rewards(rewardName))")

db.commit()
print("Database creation success.")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(956, 623)
        MainWindow.setMaximumSize(QSize(1600, 900))
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#header {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 0, 		    		134, 255), stop:1 rgba(28, 124, 31, 255));\n"
"	border-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#sideMenu {\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff\n"
"}\n"
"QPushButton {\n"
"	padding: 10px;\n"
"	background-color: rgb(85, 85, 127);\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#mainMenu {\n"
"	background-color: #1f232a;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setFrameShape(QFrame.Box)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.appname = QLabel(self.frame_3)
        self.appname.setObjectName(u"appname")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.appname.setFont(font1)
        self.appname.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.appname)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QCustomSlideMenu(self.frame_2)
        self.sideMenu.setObjectName(u"sideMenu")
        sizePolicy.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 15)
        self.appIcon = QFrame(self.sideMenu)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setFrameShape(QFrame.StyledPanel)
        self.appIcon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.appIcon)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.appIcon)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMouseTracking(False)
        self.label_10.setStyleSheet(u"image: url(:/logo/logo/logo_1.2.png);")

        self.verticalLayout_11.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.appIcon)

        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setKerning(True)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.homeBtn = QPushButton(self.frame_4)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.profileBtn = QPushButton(self.frame_4)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon2)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.profileBtn)

        self.redeemBtn = QPushButton(self.frame_4)
        self.redeemBtn.setObjectName(u"redeemBtn")
        self.redeemBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemBtn.setIcon(icon3)
        self.redeemBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.redeemBtn)

        self.recordsBtn = QPushButton(self.frame_4)
        self.recordsBtn.setObjectName(u"recordsBtn")
        self.recordsBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordsBtn.setIcon(icon4)
        self.recordsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.recordsBtn)

        self.junkBtn = QPushButton(self.frame_4)
        self.junkBtn.setObjectName(u"junkBtn")
        self.junkBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/map-pin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.junkBtn.setIcon(icon5)
        self.junkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.junkBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.mainMenu = QFrame(self.frame_2)
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_12 = QVBoxLayout(self.home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_7 = QWidget(self.home)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_13 = QVBoxLayout(self.widget_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.widget_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.homeName = QLabel(self.frame_7)
        self.homeName.setObjectName(u"homeName")
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.homeName.setFont(font3)
        self.homeName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.homeName)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.stack_holder = QFrame(self.widget_7)
        self.stack_holder.setObjectName(u"stack_holder")
        self.stack_holder.setStyleSheet(u"#stack_holder {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.stack_holder.setFrameShape(QFrame.StyledPanel)
        self.stack_holder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.stack_holder)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget_2 = QStackedWidget(self.stack_holder)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.description = QWidget()
        self.description.setObjectName(u"description")
        self.verticalLayout_10 = QVBoxLayout(self.description)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.description)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_11.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_11)

        self.textEdit = QTextEdit(self.description)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.frame_6 = QFrame(self.description)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rewardBtn = QPushButton(self.frame_6)
        self.rewardBtn.setObjectName(u"rewardBtn")
        self.rewardBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rewardBtn.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.rewardBtn)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.stackedWidget_2.addWidget(self.description)
        self.reward = QWidget()
        self.reward.setObjectName(u"reward")
        self.verticalLayout_17 = QVBoxLayout(self.reward)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_5 = QLabel(self.reward)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_5)

        self.scrollArea = QScrollArea(self.reward)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setStyleSheet(u"/*HORIZONTAL*/\n"
"\n"
"QcrollBar:horizontal {\n"
"	border: none;\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(39, 40, 101);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(39, 40, 101);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizintal:pressed{\n"
"	background-color: #fff;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 686, 336))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 2218, 301))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.rewardHold = QFrame(self.scrollAreaWidgetContents_2)
        self.rewardHold.setObjectName(u"rewardHold")
        self.rewardHold.setMinimumSize(QSize(2200, 0))
        self.rewardHold.setFrameShape(QFrame.StyledPanel)
        self.rewardHold.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.rewardHold)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_36 = QFrame(self.rewardHold)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"#frame_36 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_36)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_44 = QFrame(self.frame_36)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"image: url(:/junk/misc pic/junk items/bottle.png);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.verticalLayout_52.addWidget(self.frame_44)


        self.horizontalLayout_11.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.rewardHold)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"#frame_37 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_37)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_45 = QFrame(self.frame_37)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"image: url(:/junk/misc pic/junk items/cans.png);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.verticalLayout_51.addWidget(self.frame_45)


        self.horizontalLayout_11.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.rewardHold)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"#frame_38 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_38)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_46 = QFrame(self.frame_38)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"image: url(:/junk/misc pic/junk items/carton.png);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.verticalLayout_50.addWidget(self.frame_46)


        self.horizontalLayout_11.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.rewardHold)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"#frame_39 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_39)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_47 = QFrame(self.frame_39)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"image: url(:/junk/misc pic/junk items/electrical.png);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.verticalLayout_49.addWidget(self.frame_47)


        self.horizontalLayout_11.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.rewardHold)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"#frame_40 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_40)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_48 = QFrame(self.frame_40)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"image: url(:/junk/misc pic/junk items/metals.png);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.verticalLayout_48.addWidget(self.frame_48)


        self.horizontalLayout_11.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.rewardHold)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"#frame_41 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_41)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_49 = QFrame(self.frame_41)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"image: url(:/junk/misc pic/junk items/paper.png);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_49)


        self.horizontalLayout_11.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.rewardHold)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"#frame_42 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_42)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_50 = QFrame(self.frame_42)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"image: url(:/junk/misc pic/junk items/plastics.png);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)

        self.verticalLayout_45.addWidget(self.frame_50)


        self.horizontalLayout_11.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.rewardHold)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"#frame_43 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_43)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_51 = QFrame(self.frame_43)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"image: url(:/junk/misc pic/junk items/tires.png);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_51)


        self.horizontalLayout_11.addWidget(self.frame_43)


        self.verticalLayout_44.addWidget(self.rewardHold)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_8.addWidget(self.scrollArea_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)

        self.frame_8 = QFrame(self.reward)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.wnBtn = QPushButton(self.frame_8)
        self.wnBtn.setObjectName(u"wnBtn")
        self.wnBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wnBtn.setIcon(icon7)

        self.verticalLayout_18.addWidget(self.wnBtn)


        self.verticalLayout_17.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.reward)

        self.verticalLayout_15.addWidget(self.stackedWidget_2)


        self.verticalLayout_13.addWidget(self.stack_holder)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.home)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_6 = QVBoxLayout(self.profile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.profile)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.profileTitle = QLabel(self.frame_5)
        self.profileTitle.setObjectName(u"profileTitle")
        self.profileTitle.setFont(font1)

        self.horizontalLayout_6.addWidget(self.profileTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_52 = QFrame(self.profile)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"#frame_5 {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.frame_52)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.details = QFrame(self.frame_52)
        self.details.setObjectName(u"details")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy3)
        self.details.setStyleSheet(u"")
        self.details.setFrameShape(QFrame.StyledPanel)
        self.details.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.details)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.columnA = QFrame(self.details)
        self.columnA.setObjectName(u"columnA")
        self.columnA.setMaximumSize(QSize(150, 16777215))
        self.columnA.setFrameShape(QFrame.StyledPanel)
        self.columnA.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.columnA)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.columnA)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.columnA)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_9.addWidget(self.label_2)

        self.label_6 = QLabel(self.columnA)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_8 = QLabel(self.columnA)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.columnA)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_9 = QLabel(self.columnA)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.columnA, 0, Qt.AlignHCenter)

        self.columnB = QFrame(self.details)
        self.columnB.setObjectName(u"columnB")
        self.columnB.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:Focus {\n"
"	border: 2px solid #0000ff;\n"
"}")
        self.columnB.setFrameShape(QFrame.StyledPanel)
        self.columnB.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.columnB)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.memLine = QLineEdit(self.columnB)
        self.memLine.setObjectName(u"memLine")
        self.memLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.memLine)

        self.userLine = QLineEdit(self.columnB)
        self.userLine.setObjectName(u"userLine")
        self.userLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.userLine)

        self.fnLine = QLineEdit(self.columnB)
        self.fnLine.setObjectName(u"fnLine")
        self.fnLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.fnLine)

        self.lnLine = QLineEdit(self.columnB)
        self.lnLine.setObjectName(u"lnLine")
        self.lnLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.lnLine)

        self.contLine = QLineEdit(self.columnB)
        self.contLine.setObjectName(u"contLine")
        self.contLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.contLine)

        self.emailLine = QLineEdit(self.columnB)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.emailLine)


        self.horizontalLayout_4.addWidget(self.columnB)


        self.verticalLayout_7.addWidget(self.details)

        self.logout = QFrame(self.frame_52)
        self.logout.setObjectName(u"logout")
        self.logout.setMaximumSize(QSize(16777215, 55))
        self.logout.setFrameShape(QFrame.StyledPanel)
        self.logout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.logout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logOut = QPushButton(self.logout)
        self.logOut.setObjectName(u"logOut")
        self.logOut.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOut.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.logOut)

        self.updBtn = QPushButton(self.logout)
        self.updBtn.setObjectName(u"updBtn")
        self.updBtn.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.updBtn)

        self.pushButton = QPushButton(self.logout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.logout, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_52)

        self.stackedWidget.addWidget(self.profile)
        self.redeem = QWidget()
        self.redeem.setObjectName(u"redeem")
        self.redeem.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:Focus {\n"
"	border: 2px solid #0000ff;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.redeem)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.redeemFrame = QFrame(self.redeem)
        self.redeemFrame.setObjectName(u"redeemFrame")
        self.redeemFrame.setMaximumSize(QSize(16777215, 80))
        self.redeemFrame.setStyleSheet(u"")
        self.redeemFrame.setFrameShape(QFrame.StyledPanel)
        self.redeemFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.redeemFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_11 = QFrame(self.redeemFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)


        self.horizontalLayout_9.addWidget(self.frame_11)

        self.pointBox = QWidget(self.redeemFrame)
        self.pointBox.setObjectName(u"pointBox")
        self.horizontalLayout_10 = QHBoxLayout(self.pointBox)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.pointBox)
        self.label_13.setObjectName(u"label_13")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_13.setFont(font6)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.lineEdit = QLineEdit(self.pointBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_10.addWidget(self.lineEdit)


        self.horizontalLayout_9.addWidget(self.pointBox, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.redeemFrame)

        self.frame_10 = QFrame(self.redeem)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"#frame_10 {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.redeemGrid = QFrame(self.frame_10)
        self.redeemGrid.setObjectName(u"redeemGrid")
        self.redeemGrid.setStyleSheet(u"")
        self.redeemGrid.setFrameShape(QFrame.StyledPanel)
        self.redeemGrid.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.redeemGrid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.redeemGrid)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_12 = QFrame(self.widget)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/gcash_500.jpg);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.gcash = QPushButton(self.frame_13)
        self.gcash.setObjectName(u"gcash")
        self.gcash.setFont(font)

        self.verticalLayout_30.addWidget(self.gcash)


        self.verticalLayout_22.addWidget(self.frame_13)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.redeemGrid)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_14 = QFrame(self.widget_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/grab_200.jpg);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.widget_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.grab = QPushButton(self.frame_15)
        self.grab.setObjectName(u"grab")
        self.grab.setFont(font)

        self.verticalLayout_31.addWidget(self.grab)


        self.verticalLayout_23.addWidget(self.frame_15)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.redeemGrid)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_24 = QVBoxLayout(self.widget_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_16 = QFrame(self.widget_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/lazada_100.jpg);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.widget_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_17)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lazada = QPushButton(self.frame_17)
        self.lazada.setObjectName(u"lazada")
        self.lazada.setFont(font)

        self.verticalLayout_32.addWidget(self.lazada)


        self.verticalLayout_24.addWidget(self.frame_17)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_4 = QWidget(self.redeemGrid)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_25 = QVBoxLayout(self.widget_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_18 = QFrame(self.widget_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/robinsons_1000.jpg);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.widget_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_19)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.robinsons = QPushButton(self.frame_19)
        self.robinsons.setObjectName(u"robinsons")
        self.robinsons.setFont(font)

        self.verticalLayout_29.addWidget(self.robinsons)


        self.verticalLayout_25.addWidget(self.frame_19)


        self.gridLayout.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.redeemGrid)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_26 = QVBoxLayout(self.widget_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_20 = QFrame(self.widget_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/nbs_500.jpg);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.widget_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_21)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.national = QPushButton(self.frame_21)
        self.national.setObjectName(u"national")
        self.national.setFont(font)

        self.verticalLayout_28.addWidget(self.national)


        self.verticalLayout_26.addWidget(self.frame_21)


        self.gridLayout.addWidget(self.widget_5, 1, 1, 1, 1)

        self.widget_6 = QWidget(self.redeemGrid)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_27 = QVBoxLayout(self.widget_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_22 = QFrame(self.widget_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"image: url(:/giftCards/misc pic/gift cards/smdept_500.jpg);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.widget_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_23)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.sm = QPushButton(self.frame_23)
        self.sm.setObjectName(u"sm")
        self.sm.setFont(font)

        self.verticalLayout_33.addWidget(self.sm)


        self.verticalLayout_27.addWidget(self.frame_23)


        self.gridLayout.addWidget(self.widget_6, 1, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.redeemGrid)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.redeem)
        self.records = QWidget()
        self.records.setObjectName(u"records")
        self.verticalLayout_35 = QVBoxLayout(self.records)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_14 = QLabel(self.records)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setPointSize(30)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_14.setFont(font7)

        self.verticalLayout_35.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.frame_29 = QFrame(self.records)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setStyleSheet(u"#frame_29 {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_29)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_53 = QFrame(self.frame_29)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"#frame_53 {\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.recordTable = QTableWidget(self.frame_53)
        if (self.recordTable.columnCount() < 5):
            self.recordTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.recordTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.recordTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.recordTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.recordTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.recordTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.recordTable.setObjectName(u"recordTable")
        self.recordTable.setGeometry(QRect(70, 10, 722, 433))
        self.recordTable.setStyleSheet(u"/*HORIZONTAL*/\n"
"\n"
"QcrollBar:horizontal {\n"
"	border: none;\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(39, 40, 101);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(39, 40, 101);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizintal:pressed{\n"
"	background-color: #fff;\n"
"}")

        self.verticalLayout_36.addWidget(self.frame_53)


        self.verticalLayout_35.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.records)
        self.shops = QWidget()
        self.shops.setObjectName(u"shops")
        self.verticalLayout_19 = QVBoxLayout(self.shops)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_4 = QLabel(self.shops)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_4)

        self.frame_9 = QFrame(self.shops)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"#frame_9 {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_9)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.shopFrame = QFrame(self.frame_9)
        self.shopFrame.setObjectName(u"shopFrame")
        self.shopFrame.setFrameShape(QFrame.StyledPanel)
        self.shopFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.shopFrame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.scrollArea_3 = QScrollArea(self.shopFrame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 120))
        self.scrollArea_3.setStyleSheet(u"/*VERTICAL*/\n"
"\n"
"QcrollBar:vertical {\n"
"	border: none;\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(39, 40, 101);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(39, 40, 101);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"/*HORIZONTAL*/\n"
"\n"
"QcrollBar:horizontal {\n"
"	border: none;\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius: 0"
                        "px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(39, 40, 101);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1518, 618))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.shopLoc = QFrame(self.scrollAreaWidgetContents_3)
        self.shopLoc.setObjectName(u"shopLoc")
        self.shopLoc.setMinimumSize(QSize(1500, 600))
        self.shopLoc.setFrameShape(QFrame.StyledPanel)
        self.shopLoc.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.shopLoc)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_25 = QFrame(self.shopLoc)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"#frame_25 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_25)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_24 = QFrame(self.frame_25)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"image: url(:/shops/misc pic/shops/fnj.jpg);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame_24)

        self.label_15 = QLabel(self.frame_25)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 50))
        self.label_15.setFont(font)

        self.verticalLayout_38.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_25, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.shopLoc)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"#frame_26 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_26)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_32 = QFrame(self.frame_26)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"image: url(:/shops/misc pic/shops/dadtata.jpg);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.frame_32)

        self.label_16 = QLabel(self.frame_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setFont(font)

        self.verticalLayout_39.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_26, 0, 1, 1, 1)

        self.frame_27 = QFrame(self.shopLoc)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"#frame_27 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_27)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_33 = QFrame(self.frame_27)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"image: url(:/shops/misc pic/shops/no_image.jpg);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.frame_33)

        self.label_17 = QLabel(self.frame_27)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setFont(font)

        self.verticalLayout_40.addWidget(self.label_17, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_27, 0, 2, 1, 1)

        self.frame_28 = QFrame(self.shopLoc)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_28 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_28)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_34 = QFrame(self.frame_28)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"image: url(:/shops/misc pic/shops/no_image.jpg);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.frame_34)

        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 50))
        self.label_18.setFont(font)

        self.verticalLayout_41.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_28, 1, 0, 1, 1)

        self.frame_30 = QFrame(self.shopLoc)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"#frame_30 {\n"
"	background-color: #55557f;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_30)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"image: url(:/shops/misc pic/shops/no_image.jpg);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_42.addWidget(self.frame_35)

        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setFont(font)

        self.verticalLayout_42.addWidget(self.label_19, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_30, 1, 1, 1, 1)

        self.frame_31 = QFrame(self.shopLoc)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_31)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")

        self.gridLayout_2.addWidget(self.frame_31, 1, 2, 1, 1)


        self.horizontalLayout_12.addWidget(self.shopLoc)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_37.addWidget(self.scrollArea_3)


        self.verticalLayout_34.addWidget(self.shopFrame)


        self.verticalLayout_19.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.shops)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainMenu)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"Junk N' Trade", None))
        self.label_10.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profileBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.redeemBtn.setText(QCoreApplication.translate("MainWindow", u"Redeem", None))
        self.recordsBtn.setText(QCoreApplication.translate("MainWindow", u"Records", None))
        self.junkBtn.setText(QCoreApplication.translate("MainWindow", u"Junk Shops", None))
        self.homeName.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO JUNK N' TRADE!", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Whats's Junk n Trade?", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Junk n' Trade is a waste management system that can help citizens be responsible for their waste disposal and benefit society and the environment. This could start a movement for consumers to be held accountable for every waste they create. The introduction of the reward system in our program will help motivate people to manage their waste properly.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\""
                        "><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">What's new in 1.3.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- CRUD updated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Redeem system Working</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Added records</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Records working</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Updated junk shops</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.rewardBtn.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.wnBtn.setText(QCoreApplication.translate("MainWindow", u"What's JNT?", None))
        self.profileTitle.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Member ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contact No.:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email Address:", None))
        self.memLine.setPlaceholderText("")
        self.userLine.setPlaceholderText("")
        self.fnLine.setPlaceholderText("")
        self.lnLine.setPlaceholderText("")
        self.contLine.setPlaceholderText("")
        self.emailLine.setPlaceholderText("")
        self.logOut.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.updBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE PROFILE", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE ACCOUNT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REDEEM", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"POINTS", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.gcash.setText(QCoreApplication.translate("MainWindow", u"GCash 500 - 5000pts", None))
        self.grab.setText(QCoreApplication.translate("MainWindow", u"Grab 200 - 2000pts", None))
        self.lazada.setText(QCoreApplication.translate("MainWindow", u"Lazada 100 - 1000pts", None))
        self.robinsons.setText(QCoreApplication.translate("MainWindow", u"Robinsons 1000 - 10000pts", None))
        self.national.setText(QCoreApplication.translate("MainWindow", u"National 500 - 5000pts", None))
        self.sm.setText(QCoreApplication.translate("MainWindow", u"SM 500 - 5000pts", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Records", None))
        ___qtablewidgetitem = self.recordTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"recordID", None));
        ___qtablewidgetitem1 = self.recordTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"memberID", None));
        ___qtablewidgetitem2 = self.recordTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"rewardName", None));
        ___qtablewidgetitem3 = self.recordTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"rewardAmount", None));
        ___qtablewidgetitem4 = self.recordTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"date", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"JUNK SHOPS", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"F & J Junk Shop - 139 20th Ave, Cubao, Quezon City, 1109 Metro Manila", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Dadtata Junk Shop - 8 Dao Cor Tindalo, Project 3, Quezon City, 1102 Metro Manila", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"MCI Junk Shop - 823, Aurora Boulevard, Cubao, Quezon City, 1109 Metro Manila", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Aves Junk Shop - 37 F. Castillo, Project 4, Quezon City, 1109 Metro Manila", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Montanges Junk Shop - 139 20th Ave, Cubao, Quezon City, 1109 Metro Manila", None))

        self.memLine.setEnabled(False)
        self.userLine.setEnabled(False)
        self.lineEdit.setEnabled(False)
    # retranslateUi

