from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(309, 238)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_4.setStyleSheet("font-size: 8pt")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 51, 21))
        self.pushButton.setStyleSheet("background-color: rgb(120, 178, 88);\n"
"")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 120, 171, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 8pt\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 150, 171, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 8pt\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 311, 41))
        self.label.setStyleSheet("background-color: rgb(155, 231, 113); \n"
"font: 20pt \"Century Gothic\";\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 210, 51, 16))
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
"font: 8pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 99, 0);\n"
"border-bottom: 2px solid(0, 90, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_5.setStyleSheet("font-size: 8pt")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_3.setStyleSheet("font-size: 8pt")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 8pt\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 51, 16))
        self.label_6.setStyleSheet("font-size: 8pt")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 8pt\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 210, 101, 16))
        self.label_9.setStyleSheet("font: 8pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "Welcome To Fresh Box"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "No. HP"))
        self.label_9.setText(_translate("MainWindow", "Sudah Punya Akun?"))
