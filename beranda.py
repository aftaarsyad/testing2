# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beranda.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QFileDialog
import pyaudio
import wave
import datetime
import os


conn = None
con = pymysql.connect(db='skripsi', user='root', passwd='', 
                      host='localhost',port=3306, autocommit=True)
kursor = con.cursor()


class beranda(QtWidgets.QMainWindow): #Window Beranda
    def __init__(self, parent=None):
        super(beranda, self).__init__()
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 10, 630, 60))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 50, 630, 60))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(35, 90, 630, 60))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.logoupn = QtWidgets.QLabel(self.centralwidget)
        self.logoupn.setGeometry(QtCore.QRect(240, 170, 251, 211))
        self.logoupn.setText("")
        self.logoupn.setPixmap(QtGui.QPixmap("logo_upn.png"))
        self.logoupn.setScaledContents(True)
        self.logoupn.setAlignment(QtCore.Qt.AlignCenter)
        self.logoupn.setObjectName("logoupn")
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
        self.label.setText(_translate("MainWindow", "Aplikasi Pendeteksi Kesalahan Hukum Baca Tajwid"))
        self.label_2.setText(_translate("MainWindow", " menggunakan Metode Mel Frequency Cepstrum Coefficient"))
        self.label_3.setText(_translate("MainWindow", "dengan Fast Fourier Transform"))
        self.menuBeranda.setTitle(_translate("MainWindow", "Beranda"))
        self.menuLatihan.setTitle(_translate("MainWindow", "Latihan"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionBeranda.setText(_translate("MainWindow", "Beranda"))
        self.actionLatihan.setText(_translate("MainWindow", "Latihan"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        
        self.actionLogin.triggered.connect(self.tampil_login)
        self.actionLatihan.triggered.connect(self.tampil_latihan)
        
    def tampil_latihan(self):
        self.mainwindow2 = latih(self)
        self.mainwindow2.setupUi(MainWindow)
        
    def tampil_login(self):
        self.mainwindow3 = admlogin(self)
        self.mainwindow3.setupUi(MainWindow)

class latih(QtWidgets.QMainWindow): #Window Latihan
    def __init__(self, parent=None):
        super(latih, self).__init__()
        self.setupUi(MainWindow)
        
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
        self.comboBox.addItem("Logo")
        self.comboBox.addItem("nama1")
        self.comboBox.addItem("nama2")
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
        self.comboBox.setItemText(0, _translate("MainWindow", "Logo"))
        self.comboBox.setItemText(1, _translate("MainWindow", "nama1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "nama2"))
        self.btnpilihFoto.setText(_translate("MainWindow", "Pilih"))
        self.menuBeranda.setTitle(_translate("MainWindow", "Beranda"))
        self.menuLatihan.setTitle(_translate("MainWindow", "Latihan"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionBeranda.setText(_translate("MainWindow", "Beranda"))
        self.actionLatihan.setText(_translate("MainWindow", "Latihan"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))

        self.actionBeranda.triggered.connect(self.tampil_beranda)
        self.actionLogin.triggered.connect(self.tampil_login)
        self.btnPilihFile.clicked.connect(self.bukafile)
        self.btnRekam.clicked.connect(self.rekam)
        self.btnpilihFoto.clicked.connect(self.tampil_foto)
        
        
    def tampil_beranda(self):
        self.mainwindow4 = beranda(self)
        self.mainwindow4.setupUi(MainWindow)
        
    def tampil_login(self):
        self.mainwindow5 = admlogin(self)
        self.mainwindow5.setupUi(MainWindow)
    
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
           
    def tampil_foto(self):
        if self.comboBox.currentIndex() == 0:
            self.gbrTajwid.setPixmap(QtGui.QPixmap("imgs/logo.png"))
        elif self.comboBox.currentIndex() == 1:
            self.gbrTajwid.setPixmap(QtGui.QPixmap("imgs/nama1.png"))
        else:
            self.gbrTajwid.setPixmap(QtGui.QPixmap("imgs/logo.png"))
    
    def bukafile(self):
        pilihnamafile = QFileDialog.getOpenFileName(None, 'Pilih File Suara yang akan dideteksi')
        path = pilihnamafile[0]
        self.lokasiFile.setText(path)
        
    def rekam(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        
        nama = self.lblNama.text()
        if nama == "":
            self.messagebox("Alert","Masukkan nama Anda!")
        else:
            p = pyaudio.PyAudio()
            #Mulai Perekaman
        
            print("* recording")
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            frames = []
            startDateTimeStr = datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S")
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            fileName = nama + startDateTimeStr + ".wav"
            print("* done recording")
        

            stream.stop_stream()
            stream.close()
            p.terminate()
        
            waveFile = wave.open(fileName, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(p.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()
        
            pathrekam = os.path.realpath(fileName)
            self.lokasiFile.setText(pathrekam)
        
class admlogin(QtWidgets.QMainWindow): #Window Admin
    def __init__(self, parent=None):
        super(admlogin, self).__init__()
        self.setupUi(MainWindow)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Form = QtWidgets.QLabel(self.centralwidget)
        self.Form.setGeometry(QtCore.QRect(275, 60, 150, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Form.setFont(font)
        self.Form.setAlignment(QtCore.Qt.AlignCenter)
        self.Form.setObjectName("Form")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 120, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 120, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.userLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.userLogin.setGeometry(QtCore.QRect(280, 120, 200, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.userLogin.setFont(font)
        self.userLogin.setObjectName("userLogin")
        self.passLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.passLogin.setGeometry(QtCore.QRect(280, 190, 200, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passLogin.setFont(font)
        self.passLogin.setObjectName("passLogin")
        
        self.passLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(330, 260, 150, 40))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
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
        self.Form.setText(_translate("MainWindow", "Login Admin"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.menuBeranda.setTitle(_translate("MainWindow", "Beranda"))
        self.menuLatihan.setTitle(_translate("MainWindow", "Latihan"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionBeranda.setText(_translate("MainWindow", "Beranda"))
        self.actionLatihan.setText(_translate("MainWindow", "Latihan"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        
        self.actionBeranda.triggered.connect(self.tampil_beranda)
        self.actionLatihan.triggered.connect(self.tampil_latihan)
        self.btnLogin.clicked.connect(self.masuk_admin)
        
    def tampil_beranda(self):
        self.mainwindow6 = beranda(self)
        self.mainwindow6.setupUi(MainWindow)
    
    def tampil_latihan(self):
        self.mainwindow7 = latih(self)
        self.mainwindow7.setupUi(MainWindow)
    
    
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def masuk_admin(self):
        username = self.userLogin.text()
        password = self.passLogin.text()
        kursor = con.cursor()
        query = "select * from admin where username=%s and password=%s"
        data = kursor.execute(query,(username,password))
        if(data):
            self.window = QtWidgets.QMainWindow()
            self.ui = menuadmin()
            self.ui.setupUi(self.window)
        else:
            self.messagebox("Alert","Username atau Password Salah !")
        
class menuadmin(QtWidgets.QMainWindow): #Window Menu Admin
    def __init__(self, parent=None):
        super(menuadmin, self).__init__()
        self.setupUi(MainWindow)
        
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
        
        self.btnTambahAdmin.clicked.connect(self.tampil_tambahAdmin)
        
    def tampil_tambahAdmin(self):
        self.mainwindow8 = tambahAdmin(self)
        self.mainwindow8.setupUi(MainWindow)


class tambahAdmin(QtWidgets.QMainWindow): #Window Menu Tambah Admin
    def __init__(self, parent=None):
        super(tambahAdmin, self).__init__()
        self.setupUi(MainWindow)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 150, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 120, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 120, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 120, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lblUserTambah = QtWidgets.QLineEdit(self.centralwidget)
        self.lblUserTambah.setGeometry(QtCore.QRect(170, 100, 200, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblUserTambah.setFont(font)
        self.lblUserTambah.setObjectName("lblUserTambah")
        self.lblPassTambah = QtWidgets.QLineEdit(self.centralwidget)
        self.lblPassTambah.setGeometry(QtCore.QRect(170, 150, 200, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblPassTambah.setFont(font)
        self.lblPassTambah.setObjectName("lblPassTambah")
        
        self.lblPassTambah.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.lblRepassTambah = QtWidgets.QLineEdit(self.centralwidget)
        self.lblRepassTambah.setGeometry(QtCore.QRect(170, 200, 200, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblRepassTambah.setFont(font)
        self.lblRepassTambah.setObjectName("lblRepassTambah")
        
        self.lblRepassTambah.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.btnBuatAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuatAdmin.setGeometry(QtCore.QRect(270, 260, 100, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnBuatAdmin.setFont(font)
        self.btnBuatAdmin.setObjectName("btnBuatAdmin")
        self.btnKembali = QtWidgets.QPushButton(self.centralwidget)
        self.btnKembali.setGeometry(QtCore.QRect(170, 260, 100, 30))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tambah Admin"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Re-Password"))
        self.btnBuatAdmin.setText(_translate("MainWindow", "Buat"))
        self.btnKembali.setText(_translate("MainWindow", "Kembali"))
    
        self.btnBuatAdmin.clicked.connect(self.buat_admin_baru)
        self.btnKembali.clicked.connect(self.tampil_menu_admin)
        
    def tampil_menu_admin(self):
        self.mainwindow9 = menuadmin(self)
        self.mainwindow9.setupUi(MainWindow)
    
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
            
    def buat_admin_baru(self):
        kursor = con.cursor()
        kursor.execute("Select * From admin")
        jml = kursor.fetchall()
        jumlah = len(jml)
        user = self.lblUserTambah.text()
        passwd = self.lblPassTambah.text()
        repasswd = self.lblRepassTambah.text()
        insert = (jumlah+1, user, passwd, repasswd)
        if user == "" or passwd == "" or repasswd == "":
            self.messagebox("Alert","Username/Password/Re-Password Tidak Boleh Kosong !")
        elif passwd != repasswd:
            self.messagebox("Alert", "Password dan Re-Password Harus Sama")
        else:
            sql = "INSERT INTO admin (id_admin, username, password, repassword)" + "VALUES" + str(insert)
            data = kursor.execute(sql)
            if(data):
                self.messagebox("Congrats","Berhasil Buat !")
            else:
                self.messagebox("Alert","Failed !")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = beranda()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())