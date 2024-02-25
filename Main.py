from PyQt5 import QtCore, QtGui, QtWidgets

username = "levani"
password = "123456789"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 542)
        MainWindow.setStyleSheet("background-color: rgb(67, 67, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 411, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("login.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.login)
        self.lineEdit.setGeometry(QtCore.QRect(120, 230, 161, 31))
        self.lineEdit.setStyleSheet("QLineEdit:hover{\n"
"border:2px solid rgb(48, 50, 62);\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.login)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 300, 161, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit:hover{\n"
"border:2px solid rgb(48, 50, 62);\n"
"}")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.login)
        self.pushButton.setGeometry(QtCore.QRect(130, 390, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.login)
        self.label_3.setGeometry(QtCore.QRect(120, 350, 161, 20))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.login)
        self.successful = QtWidgets.QWidget()
        self.successful.setObjectName("successful")
        self.label_2 = QtWidgets.QLabel(self.successful)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 231, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("welcome.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.successful)
        self.label_4.setGeometry(QtCore.QRect(120, 320, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.successful)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 440, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.successful)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWinldow", "Log In"))
        self.label_4.setText(_translate("MainWindow", "Successful"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))

    def check(self):
        entered_username = self.lineEdit.text()
        entered_password = self.lineEdit_2.text()

        if entered_username == username and entered_password == password:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.label_3.setText("incorrect username or password")
            self.label_3.setStyleSheet("color : red;")

    def exit(self):
        self.stackedWidget.setCurrentIndex(0)
        self.label_3.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
