# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 356)
        MainWindow.setStyleSheet("background-color: rgb(43, 53, 79)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.StreamdjLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.StreamdjLabel.setGeometry(QtCore.QRect(130, 20, 241, 20))
        self.StreamdjLabel.setStyleSheet("border:none;\n"
"color:rgb(204, 167, 71);\n"
"font: 63 11pt \"Source Sans Pro Semibold\";\n"
"background-color:rgb(67, 67, 125);")
        self.StreamdjLabel.setObjectName("StreamdjLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setStyleSheet("font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.label_2.setStyleSheet("font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72)")
        self.label_2.setObjectName("label_2")
        self.MusicurlLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.MusicurlLabel.setGeometry(QtCore.QRect(130, 60, 241, 20))
        self.MusicurlLabel.setStyleSheet("color:rgb(204, 167, 71);\n"
"border:none;\n"
"font: 63 11pt \"Source Sans Pro Semibold\";\n"
"background-color:rgb(67, 67, 125);\n"
"")
        self.MusicurlLabel.setObjectName("MusicurlLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 51, 31))
        self.label_3.setStyleSheet("font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72)")
        self.label_3.setObjectName("label_3")
        self.AuthorLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthorLabel.setGeometry(QtCore.QRect(130, 100, 241, 20))
        self.AuthorLabel.setStyleSheet("color:rgb(204, 167, 71);\n"
"border:none;\n"
"font: 63 11pt \"Source Sans Pro Semibold\";\n"
"background-color:rgb(67, 67, 125);\n"
"\n"
"")
        self.AuthorLabel.setObjectName("AuthorLabel")
        self.OrderButton = QtWidgets.QPushButton(self.centralwidget)
        self.OrderButton.setGeometry(QtCore.QRect(110, 140, 131, 41))
        self.OrderButton.setStyleSheet("QPushButton{\n"
"font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72);\n"
"background-color: rgb(63, 78, 116);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(77, 95, 141);\n"
"color:rgb(234, 191, 81)\n"
"}")
        self.OrderButton.setObjectName("OrderButton")

        self.LOGS = QtWidgets.QLabel(self.centralwidget)
        self.LOGS.setGeometry(QtCore.QRect(16, 192, 171, 121))
        self.LOGS.setStyleSheet("font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72)")
        self.LOGS.setText("")
        self.LOGS.setObjectName("LOGS")
        self.BreakButton = QtWidgets.QPushButton(self.centralwidget)
        self.BreakButton.setGeometry(QtCore.QRect(240, 290, 121, 31))
        self.BreakButton.setStyleSheet("QPushButton{\n"
"font: 63 11pt \"Source Sans Pro Semibold\";\n"
"color: rgb(208, 170, 72);\n"
"background-color: rgb(63, 78, 116);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(77, 95, 141);\n"
"color:rgb(234, 191, 81)\n"
"}")
        self.BreakButton.setObjectName("BreakButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StreamDJ order"))
        self.label.setText(_translate("MainWindow", "StreamDJ channel: "))
        self.label_2.setText(_translate("MainWindow", "        Url to song or\n"
"                     playlist:"))
        self.label_3.setText(_translate("MainWindow", "Author:"))
        self.OrderButton.setText(_translate("MainWindow", "Order"))
        self.BreakButton.setText(_translate("MainWindow", "Abort order"))