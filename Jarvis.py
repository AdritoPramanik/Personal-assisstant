# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jarvis.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 1400, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/IronMan.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 606, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"background:transparent;\n"
"color:white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1040, 600, 75, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background:transparent")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -60, 421, 200))
        self.label_2.setStyleSheet("background:transparent")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/initializingSystem.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(550, 20, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:blue;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(880, 20, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:blue;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 171, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 171, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 171, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 400, 171, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 171, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1200, 450, 161, 260))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/rotate.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(910, 600, 111, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM (1).jpeg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1030, 600, 91, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/exit.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 580, 241, 131))
        self.label_11.setText("")
        # self.label_11.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/bottom design.gif"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 280, 171, 51))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 171, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:/Users/hp/Downloads/WhatsApp Image 2021-01-12 at 9.55.05 PM.jpeg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label.raise_()
        self.label_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pushButton.raise_()
        self.label_10.raise_()
        self.pushButton_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
