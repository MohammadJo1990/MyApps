# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 626)
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(60, 90, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelFirstNumber.setFont(font)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(60, 170, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSecondNumber.setFont(font)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(30, 440, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(292, 100, 181, 41))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(292, 170, 181, 41))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(40, 320, 93, 28))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(190, 320, 93, 28))
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(350, 320, 93, 28))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(530, 320, 93, 28))
        self.pushButtonDivide.setObjectName("pushButtonDivide")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number "))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "*"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))
