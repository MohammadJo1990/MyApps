# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCreateTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(986, 772)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 331, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 260, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(380, 250, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(50, 590, 871, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResponse.setFont(font)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setGeometry(QtCore.QRect(390, 60, 421, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditDBName.setFont(font)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setGeometry(QtCore.QRect(390, 150, 421, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditTableName.setFont(font)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setGeometry(QtCore.QRect(100, 360, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditColumnName.setFont(font)
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.ComboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.ComboBoxDataType.setGeometry(QtCore.QRect(380, 360, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ComboBoxDataType.setFont(font)
        self.ComboBoxDataType.setObjectName("ComboBoxDataType")
        self.ComboBoxDataType.addItem("")
        self.ComboBoxDataType.addItem("")
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setGeometry(QtCore.QRect(690, 350, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonAddColumn.setFont(font)
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setGeometry(QtCore.QRect(370, 450, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonCreateTable.setFont(font)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Database Name"))
        self.label_2.setText(_translate("Dialog", "Enter Table Name"))
        self.label_3.setText(_translate("Dialog", "Column name"))
        self.label_4.setText(_translate("Dialog", "data type"))
        self.ComboBoxDataType.setItemText(0, _translate("Dialog", "integer"))
        self.ComboBoxDataType.setItemText(1, _translate("Dialog", "text"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Add column"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Create Table"))
