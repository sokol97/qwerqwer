# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(302, 409)
        self.Button_sp500 = QtWidgets.QPushButton(Form)
        self.Button_sp500.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.Button_sp500.setObjectName("Button_sp500")
        self.linetgnik = QtWidgets.QLineEdit(Form)
        self.linetgnik.setGeometry(QtCore.QRect(130, 10, 171, 21))
        self.linetgnik.setObjectName("linetgnik")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label.setStyleSheet("font: 12pt \"Sylfaen\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button_sp500.setText(_translate("Form", "S&P 500"))
        self.label.setText(_translate("Form", "Ник в телеграм:"))
