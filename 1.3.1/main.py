import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtWidgets import QMainWindow
from ui_junkntrade import *
from Custom_Widgets.Widgets import *
import datetime

# global variable
currentUser = None
currentPass = None
currentMember = None
# ----------------------------------------------------------------------------------------------------------------------


class MainWindow(QMainWindow):

    def displayRecords(self):
        values = cursor.execute(f"SELECT * FROM records WHERE memberID = '{currentMember}'")

        self.ui.recordTable.setRowCount(0)

        for row, data in enumerate(values):
            self.ui.recordTable.insertRow(row)
            for column, data in enumerate(data):
                self.ui.recordTable.setItem(row, column, QTableWidgetItem(str(data)))

    def addTransaction(self, itemID, itemAmount):
        # gets the rewardPoints of user
        cursor.execute(f"SELECT rewardPoints FROM member WHERE memberID = '{currentMember}'")
        points = cursor.fetchone()
        if points[0] > itemAmount:
            # means balance is sufficient
            newBalance = points[0] - itemAmount # deduct points
            cursor.execute(f"UPDATE member SET rewardPoints = {newBalance} WHERE memberID = '{currentMember}'")

            # gets current date
            today = datetime.date.today()
            strDate = today.strftime("%B %d, %Y")

            # adds transaction in records table
            cursor.execute(f"SELECT rewardName FROM rewards WHERE rewardID = '{itemID}'")
            itemName = cursor.fetchone()

            cursor.execute("INSERT INTO records (memberID, rewardName, rewardAmount, date) VALUES \
            (?,?,?,?)", (currentMember, itemName[0], itemAmount, strDate))

            # QMessageBox
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Success")
            alert.setWindowIcon(QtGui.QIcon("settings.ico"))
            alert.setText("Redeem success")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

            # save changes to database
            db.commit()
            return

        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle("Failed")
        alert.setWindowIcon(QtGui.QIcon("settings.ico"))
        alert.setText("Insufficient Balance")
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()

    def deleteAccount(self):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle("Warning")
        alert.setWindowIcon(QtGui.QIcon("settings.ico"))
        alert.setText("Delete this account?")
        alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = alert.exec_()
        if result == QMessageBox.Yes:
            statement = f"DELETE FROM member WHERE memberID = '{currentMember}';"
            cursor.execute(statement)
            db.commit()

            # after deleting, back to log in window
            self.logoutFunction()
        else:
            return

    def logoutFunction(self):
        # clears text in QLineEdit in profile
        self.ui.fnLine.clear()
        self.ui.lnLine.clear()
        self.ui.contLine.clear()
        self.ui.emailLine.clear()

        MainAppWindow.close()
        LogInWindow.show()

    def displayProfileInfo(self):
        global currentMember
        cursor.execute(f"SELECT memberID, username FROM member WHERE username = '{currentUser}' AND password = '{currentPass}';")
        memID = cursor.fetchone()   # gets the memberID of returned SELECT statement
        currentMember = str(memID[0])
        self.ui.memLine.setText(str(memID[0]))
        self.ui.userLine.setText(str(memID[1]))
        # check if profile is updated
        cursor.execute(f"SELECT firstName FROM member WHERE memberID = '{currentMember}';")
        value = cursor.fetchone()
        # check if firstName is NULL, meaning other entries are NULL --> Display default placeholders
        if value[0] is None:
            print("Other information is NULL")
            # display default placeholder // do nothing
        else:
            # Access attributes in member table
            cursor.execute(f"SELECT firstName, lastName, contactNumber, emailAddress FROM member WHERE memberID = '{currentMember}';")
            values = cursor.fetchone()
            # Assigning values from database to variables
            firstName = str(values[0])
            lastName = str(values[1])
            contactNum = str(values[2])
            emailAd = str(values[3])

            # display other information on QLineEdit
            self.ui.fnLine.setText(firstName)
            self.ui.lnLine.setText(lastName)
            self.ui.contLine.setText(contactNum)
            self.ui.emailLine.setText(emailAd)

    def updateProfile(self):
        firstName = self.ui.fnLine.text()
        lastName = self.ui.lnLine.text()
        contact = self.ui.contLine.text()
        email = self.ui.emailLine.text()

        # check if there's blank
        if firstName == '' or lastName == '' or contact == '' or email == '':
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setWindowTitle("Warning")
            alert.setWindowIcon(QtGui.QIcon("settings.ico"))
            alert.setText("Fill up all entry fields to submit.")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()
            return
        else:
            statement = f"UPDATE member SET firstName = '{firstName}', lastName = '{lastName}', contactNumber = '{contact}', emailAddress = '{email}' WHERE memberID = '{currentMember}';"
            cursor.execute(statement)
            db.commit()
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Success")
            alert.setWindowIcon(QtGui.QIcon("settings.ico"))
            alert.setText("Updating of information success")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

    def redeemUpdatePoints(self):
        cursor.execute(f"SELECT rewardPoints FROM member WHERE memberID = '{currentMember}'")
        points = cursor.fetchone()
        self.ui.lineEdit.setText(str(points[0]))

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Removing task Bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1280, 720)

        config_json = loadJsonStyle(self, self.ui)
        self.show()

        # setting up current page
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # buttons clicked
        self.ui.profileBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile))

        self.ui.redeemBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.redeem))
        self.ui.redeemBtn.clicked.connect(self.redeemUpdatePoints)

        self.ui.junkBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.shops))
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))

        self.ui.recordsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.records))
        self.ui.recordsBtn.clicked.connect(self.displayRecords)

        # buttons in home page
        self.ui.rewardBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.reward))
        self.ui.wnBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.description))
        self.ui.logOut.clicked.connect(self.logoutFunction)
        self.ui.updBtn.clicked.connect(self.updateProfile)
        self.ui.pushButton.clicked.connect(self.deleteAccount)

        # buttons in redeem page
        self.ui.gcash.clicked.connect(lambda: self.addTransaction(1, 5000))
        self.ui.grab.clicked.connect(lambda: self.addTransaction(2, 2000))
        self.ui.lazada.clicked.connect(lambda: self.addTransaction(3, 1000))
        self.ui.robinsons.clicked.connect(lambda: self.addTransaction(4, 10000))
        self.ui.national.clicked.connect(lambda: self.addTransaction(5, 5000))
        self.ui.sm.clicked.connect(lambda: self.addTransaction(6, 5000))

        # records widget table items

        # Disabling Line Edit
        self.ui.textEdit.setEnabled(False)


class Ui_LogInWindow(object):

    # button functions implementation
    def currentLogIn(self):
        global currentUser
        global currentPass
        currentUser = self.username.text()
        currentPass = self.password.text()

    def submit(self):
        # gets text within the QLineEdit
        username = self.username.text()
        password = self.password.text()

        # check if one of them is blank
        if username == '' or password == '':
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setWindowTitle("Warning")
            alert.setWindowIcon(QtGui.QIcon("settings.ico"))
            alert.setText("Fill up all entry fields to submit.")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()
        else:  # login account
            statement = f"SELECT username FROM member WHERE username = '{username}' AND password = '{password}';"
            cursor.execute(statement)

            if cursor.fetchone():  # if there's a value in fetchone(), account is existing in database
                notification = QMessageBox()
                notification.setIcon(QMessageBox.Information)
                notification.setWindowTitle("Success")
                notification.setWindowIcon(QtGui.QIcon("settings.ico"))
                notification.setText("Login success")
                notification.setStandardButtons(QMessageBox.Ok)
                notification.exec_()
                self.currentLogIn()    # sets current logged in if success
                # shows main app
                LogInWindow.close()
                MainAppWindow.displayProfileInfo()  # call to display current username and memberID of logged in account
                MainAppWindow.show()

            else:  # display login failed alert
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Warning)
                alert.setWindowTitle("Login failed")
                alert.setWindowIcon(QtGui.QIcon("settings.ico"))
                alert.setText("Account not existing")
                alert.setStandardButtons(QMessageBox.Ok)
                alert.exec_()

    def createAccount(self):
        LogInWindow.close()
        CreateAccWindow.show()  # shows account creation window

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)

        # no frame and translucent background window
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 370, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(9, 9, 361, 471))
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 0, 134, 255), stop:1 rgba(28, 124, 31, 255));\n"
            "border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.loginLabel = QtWidgets.QLabel(self.frame)
        self.loginLabel.setGeometry(QtCore.QRect(70, 50, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setObjectName("loginLabel")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(60, 150, 261, 40))
        self.username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(105,118,132,255);\n"
                                    "color:rgba(255,255,255,230);\n"
                                    "padding-bottom:7px;\n"
                                    "")
        self.username.setFrame(True)
        self.username.setDragEnabled(False)
        self.username.setReadOnly(False)
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(60, 220, 261, 40))
        self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(105,118,132,255);\n"
                                    "color:rgba(255,255,255,230);\n"
                                    "padding-bottom:7px;\n"
                                    "")
        self.password.setFrame(True)
        self.password.setDragEnabled(False)
        self.password.setReadOnly(False)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # hides characters in password entry
        self.signIn = QtWidgets.QPushButton(self.frame)
        self.signIn.setGeometry(QtCore.QRect(60, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signIn.setFont(font)
        self.signIn.setStyleSheet("QPushButton#signIn{\n"
                                  "    background-color: rgb(225, 225, 225);\n"
                                  "    border-radius:20px;\n"
                                  "}\n"
                                  "QPushButton#signIn:hover{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(255, 255, 255, 255));}\n"
                                  "\n"
                                  "QPushButton#signIn:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-tp:5px;\n"
                                  "    background-color: rgb(125, 125, 125);}")
        self.signIn.setObjectName("signIn")
        self.noAccountButton = QtWidgets.QPushButton(self.frame)
        self.noAccountButton.setGeometry(QtCore.QRect(60, 350, 261, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.noAccountButton.setFont(font)
        self.noAccountButton.setAutoFillBackground(False)
        self.noAccountButton.setStyleSheet("QPushButton#noAccountButton{\n"
                                           "    background-color: rgba(0,0,0,0);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#noAccountButton:pressed{\n"
                                           "    padding-left:5px;\n"
                                           "    padding-tp:5px;\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(47, 47, 143, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#noAccountButton:hover{    \n"
                                           "    \n"
                                           "    background-color: rgb(165, 165, 165);\n"
                                           "}")
        self.noAccountButton.setShortcut("")
        self.noAccountButton.setCheckable(False)
        self.noAccountButton.setObjectName("noAccountButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # assigning button functions
        self.signIn.clicked.connect(self.submit)
        self.noAccountButton.clicked.connect(self.createAccount)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Window"))
        self.loginLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">JUNK N TRADE</span></p></body></html>"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signIn.setText(_translate("MainWindow", "SIGN IN"))
        self.signIn.setShortcut(_translate("MainWindow", "Return"))
        self.noAccountButton.setText(_translate("MainWindow", "Don\'t have an account?"))


# --------------------------------------------------------------CREATE ACCOUNT WINDOW --------------------------------------------------------------


class Ui_createAccDialog(object):

    # button functions implementation
    def clear(self):
        self.username.clear()
        self.password.clear()
        self.confirmPass.clear()

    def createAccount(self):
        # get the value in text entries
        username = self.username.text()
        password = self.password.text()
        confirmPass = self.confirmPass.text()

        # check first if there is blank
        if username == '' or password == '' or confirmPass == '':
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setWindowTitle("Warning")
            alert.setWindowIcon(QtGui.QIcon("settings.ico"))
            alert.setText("Fill up all entry fields to submit.")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()
        else:  # check if password AND confirm password is the same
            if password != confirmPass:
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Warning)
                alert.setWindowTitle("Warning")
                alert.setWindowIcon(QtGui.QIcon("settings.ico"))
                alert.setText("Password and confirm password not matched")
                alert.setStandardButtons(QMessageBox.Ok)
                alert.exec_()
            else:
                # Check if same username in database
                cursor.execute(f"SELECT username FROM member WHERE username = '{username}'")
                if cursor.fetchone():    # means username is taken
                    alert = QMessageBox()
                    alert.setIcon(QMessageBox.Warning)
                    alert.setWindowTitle("Warning")
                    alert.setWindowIcon(QtGui.QIcon("settings.ico"))
                    alert.setText("Username already taken.")
                    alert.setStandardButtons(QMessageBox.Ok)
                    alert.exec_()
                    return
                # else create account
                cursor.execute("INSERT INTO member(username, password, rewardPoints) VALUES (?,?, 9999)", (username, password))
                db.commit()
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Information)
                alert.setWindowTitle("Success")
                alert.setWindowIcon(QtGui.QIcon("settings.ico"))
                alert.setText("Account creation success.")
                alert.setStandardButtons(QMessageBox.Ok)
                alert.exec_()

    def loginWindow(self):
        CreateAccWindow.close()
        LogInWindow.show()

    def setupUi(self, createAccDialog):
        createAccDialog.setObjectName("createAccDialog")
        createAccDialog.resize(450, 550)

        # no frame and translucent background window
        createAccDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        createAccDialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.frame = QtWidgets.QFrame(createAccDialog)
        self.frame.setGeometry(QtCore.QRect(40, 40, 380, 480))
        self.frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0625 rgba(29, 51, 64, 255), stop:1 rgba(50, 50, 50, 255));\n"
            "\n"
            "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.createAccountLabel = QtWidgets.QLabel(self.frame)
        self.createAccountLabel.setGeometry(QtCore.QRect(0, 30, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.createAccountLabel.setFont(font)
        self.createAccountLabel.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.createAccountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createAccountLabel.setObjectName("createAccountLabel")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(60, 120, 261, 40))
        self.username.setWhatsThis("")
        self.username.setStyleSheet("background-color: rgb(93, 128, 145);\n"
                                    "color: rgb(190, 190, 190);\n"
                                    "padding-bottom:7px;\n"
                                    "border-radius:0px;")
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(60, 190, 261, 40))
        self.password.setWhatsThis("")
        self.password.setStyleSheet("background-color: rgb(93, 128, 145);\n"
                                    "color: rgb(190, 190, 190);\n"
                                    "padding-bottom:7px;\n"
                                    "border-radius:0px;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # hides characters in password entry

        self.password.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.password.setObjectName("password")
        self.confirmPass = QtWidgets.QLineEdit(self.frame)
        self.confirmPass.setGeometry(QtCore.QRect(60, 260, 261, 40))
        self.confirmPass.setWhatsThis("")
        self.confirmPass.setStyleSheet("background-color: rgb(93, 128, 145);\n"
                                       "color: rgb(190, 190, 190);\n"
                                       "padding-bottom:7px;\n"
                                       "border-radius:0px;")
        self.confirmPass.setText("")
        self.confirmPass.setEchoMode(QtWidgets.QLineEdit.Password)  # hides characters in confirm pass entry
        self.confirmPass.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.confirmPass.setObjectName("confirmPass")
        self.signUp = QtWidgets.QPushButton(self.frame)
        self.signUp.setGeometry(QtCore.QRect(60, 330, 111, 41))
        self.signUp.setStyleSheet("QPushButton#signUp{\n"
                                  "    border-radius:20px;\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(244, 111, 121, 255), stop:1 rgba(255, 198, 198, 255));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#signUp:hover{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(244, 67, 80, 255), stop:1 rgba(255, 198, 198, 255));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#signUp:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-tp:5px;\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(244, 0, 18, 255), stop:1 rgba(255, 198, 198, 255));\n"
                                  "}")
        self.signUp.setObjectName("signUp")
        self.clearButton = QtWidgets.QPushButton(self.frame)
        self.clearButton.setGeometry(QtCore.QRect(210, 330, 111, 41))
        self.clearButton.setStyleSheet("QPushButton#clearButton{\n"
                                       "    border-radius:20px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 162, 148, 255), stop:1 rgba(94, 96, 120, 255));\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#clearButton:hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 162, 127, 255), stop:1 rgba(94, 96, 120, 255));\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#clearButton:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-tp:5px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(162, 162, 162, 255), stop:1 rgba(94, 96, 120, 255));\n"
                                       "}")
        self.clearButton.setObjectName("clearButton")
        self.haveAccountButton = QtWidgets.QPushButton(self.frame)
        self.haveAccountButton.setGeometry(QtCore.QRect(60, 390, 261, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.haveAccountButton.setFont(font)
        self.haveAccountButton.setAutoFillBackground(False)
        self.haveAccountButton.setStyleSheet("QPushButton#haveAccountButton{\n"
                                             "    background-color: rgba(0,0,0,0);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#haveAccountButton:pressed{\n"
                                             "    padding-left:5px;\n"
                                             "    padding-tp:5px;\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(47, 47, 143, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#haveAccountButton:hover{    \n"
                                             "    \n"
                                             "    background-color: rgb(165, 165, 165);\n"
                                             "}")
        self.haveAccountButton.setShortcut("")
        self.haveAccountButton.setCheckable(False)
        self.haveAccountButton.setObjectName("haveAccountButton")

        # assigning button functions
        self.haveAccountButton.clicked.connect(self.loginWindow)
        self.clearButton.clicked.connect(self.clear)
        self.signUp.clicked.connect(self.createAccount)

        self.retranslateUi(createAccDialog)
        QtCore.QMetaObject.connectSlotsByName(createAccDialog)

    def retranslateUi(self, createAccDialog):
        _translate = QtCore.QCoreApplication.translate
        createAccDialog.setWindowTitle(_translate("createAccDialog", "Dialog"))
        self.createAccountLabel.setText(_translate("createAccDialog",
                                                   "<html><head/><body><p><span style=\" color:#f46f79;\">Create Account</span></p></body></html>"))
        self.username.setPlaceholderText(_translate("createAccDialog", "    Username"))
        self.password.setPlaceholderText(_translate("createAccDialog", "    Password"))
        self.confirmPass.setPlaceholderText(_translate("createAccDialog", "    Confirm password"))
        self.signUp.setText(_translate("createAccDialog", "SIGN UP"))
        self.clearButton.setText(_translate("createAccDialog", "CLEAR"))
        self.haveAccountButton.setText(_translate("createAccDialog", "Already have an account?"))


# login window
app = QApplication(sys.argv)
LogInWindow = QtWidgets.QMainWindow()
ui = Ui_LogInWindow()
ui.setupUi(LogInWindow)
LogInWindow.show()

# create account window
CreateAccWindow = QtWidgets.QDialog()
CreateUi = Ui_createAccDialog()
CreateUi.setupUi(CreateAccWindow)
CreateAccWindow.hide()  # hides create account window

# main app window
MainAppWindow = MainWindow()
MainAppWindow.hide()

try:
    sys.exit(app.exec_())
except:
    print("Exiting....")
