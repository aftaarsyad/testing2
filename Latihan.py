# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Latihan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 70, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lblNama = QtWidgets.QLineEdit(self.centralwidget)
        self.lblNama.setGeometry(QtCore.QRect(110, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNama.setFont(font)
        self.lblNama.setObjectName("lblNama")
        self.btnPilihFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnPilihFile.setGeometry(QtCore.QRect(20, 270, 100, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnPilihFile.setFont(font)
        self.btnPilihFile.setObjectName("btnPilihFile")
        self.btnRekam = QtWidgets.QPushButton(self.centralwidget)
        self.btnRekam.setGeometry(QtCore.QRect(590, 270, 100, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRekam.setFont(font)
        self.btnRekam.setObjectName("btnRekam")
        self.btnProses = QtWidgets.QPushButton(self.centralwidget)
        self.btnProses.setGeometry(QtCore.QRect(590, 330, 100, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnProses.setFont(font)
        self.btnProses.setObjectName("btnProses")
        self.lokasiFile = QtWidgets.QLabel(self.centralwidget)
        self.lokasiFile.setGeometry(QtCore.QRect(140, 270, 381, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lokasiFile.setFont(font)
        self.lokasiFile.setFrameShape(QtWidgets.QFrame.Box)
        self.lokasiFile.setText("")
        self.lokasiFile.setAlignment(QtCore.Qt.AlignCenter)
        self.lokasiFile.setObjectName("lokasiFile")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 270, 47, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 380, 120, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.kesimpulan = QtWidgets.QLabel(self.centralwidget)
        self.kesimpulan.setGeometry(QtCore.QRect(140, 380, 91, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kesimpulan.setFont(font)
        self.kesimpulan.setFrameShape(QtWidgets.QFrame.Box)
        self.kesimpulan.setText("")
        self.kesimpulan.setObjectName("kesimpulan")
        self.proses = QtWidgets.QLabel(self.centralwidget)
        self.proses.setGeometry(QtCore.QRect(20, 330, 81, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.proses.setFont(font)
        self.proses.setText("")
        self.proses.setObjectName("proses")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(140, 330, 250, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 80, 110, 30))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 70, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gbrTajwid = QtWidgets.QLabel(self.centralwidget)
        self.gbrTajwid.setGeometry(QtCore.QRect(240, 80, 291, 151))
        self.gbrTajwid.setText("")
        self.gbrTajwid.setPixmap(QtGui.QPixmap("imgs/logo.png"))
        self.gbrTajwid.setScaledContents(True)
        self.gbrTajwid.setAlignment(QtCore.Qt.AlignCenter)
        self.gbrTajwid.setObjectName("gbrTajwid")
        self.btnpilihFoto = QtWidgets.QPushButton(self.centralwidget)
        self.btnpilihFoto.setGeometry(QtCore.QRect(110, 130, 110, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnpilihFoto.setFont(font)
        self.btnpilihFoto.setObjectName("btnpilihFoto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuBeranda = QtWidgets.QMenu(self.menubar)
        self.menuBeranda.setObjectName("menuBeranda")
        self.menuLatihan = QtWidgets.QMenu(self.menubar)
        self.menuLatihan.setObjectName("menuLatihan")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeranda = QtWidgets.QAction(MainWindow)
        self.actionBeranda.setObjectName("actionBeranda")
        self.actionLatihan = QtWidgets.QAction(MainWindow)
        self.actionLatihan.setObjectName("actionLatihan")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuBeranda.addAction(self.actionBeranda)
        self.menuLatihan.addAction(self.actionLatihan)
        self.menuAdmin.addAction(self.actionLogin)
        self.menubar.addAction(self.menuBeranda.menuAction())
        self.menubar.addAction(self.menuLatihan.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nama"))
        self.btnPilihFile.setText(_translate("MainWindow", "Pilih File"))
        self.btnRekam.setText(_translate("MainWindow", "Rekam"))
        self.btnProses.setText(_translate("MainWindow", "Proses"))
        self.label_2.setText(_translate("MainWindow", "atau"))
        self.label_3.setText(_translate("MainWindow", "Kesimpulan :"))
        self.label_4.setText(_translate("MainWindow", "Pilih"))
        self.btnpilihFoto.setText(_translate("MainWindow", "Pilih"))
        self.menuBeranda.setTitle(_translate("MainWindow", "Beranda"))
        self.menuLatihan.setTitle(_translate("MainWindow", "Latihan"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionBeranda.setText(_translate("MainWindow", "Beranda"))
        self.actionLatihan.setText(_translate("MainWindow", "Latihan"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
