# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 500)
        Dialog.setStyleSheet("background-color: #3a3a47;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 351, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color:#f2b824 ;\n"
"    background-color: #1d1c21;\n"
"    border: none;\n"
"    font: 12pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #f2c44e;\n"
"    background-color: #3a3c42;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #eb7b13;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 130, 381, 171))
        self.label.setStyleSheet("color: #ccc;\n"
"font: 11pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 351, 41))
        self.lineEdit.setStyleSheet("color: #e0bd3f;\n"
"background-color: #1d1c21;\n"
"border: none;\n"
"font: 11pt \"Comic Sans MS\";")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Погода"))
        self.pushButton.setText(_translate("Dialog", "Получить"))
        self.label.setText(_translate("Dialog", "Результат: "))