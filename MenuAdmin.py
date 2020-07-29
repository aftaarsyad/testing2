# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnTambahAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.btnTambahAdmin.setGeometry(QtCore.QRect(30, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnTambahAdmin.setFont(font)
        self.btnTambahAdmin.setObjectName("btnTambahAdmin")
        self.btnDataLatih = QtWidgets.QPushButton(self.centralwidget)
        self.btnDataLatih.setGeometry(QtCore.QRect(30, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDataLatih.setFont(font)
        self.btnDataLatih.setObjectName("btnDataLatih")
        self.btnDataHasil = QtWidgets.QPushButton(self.centralwidget)
        self.btnDataHasil.setGeometry(QtCore.QRect(30, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDataHasil.setFont(font)
        self.btnDataHasil.setObjectName("btnDataHasil")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Menu Admin :"))
        self.btnTambahAdmin.setText(_translate("MainWindow", "Tambah Admin"))
        self.btnDataLatih.setText(_translate("MainWindow", "Data Latih"))
        self.btnDataHasil.setText(_translate("MainWindow", "Data Hasil"))
