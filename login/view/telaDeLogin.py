# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaDeLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
from time import sleep
from hashlib import sha256
from ..model.util import isAutenticarLogin

import sys
import threading

class Ui_mainFrame(object):

    def __init__(self):
        self.statusThread = True
        t = threading.Thread(target=self.event_iniciarRelogio)
        t.start()

    def exitThread(self):
        self.statusThread = False

    def setupUi(self, mainFrame):
        mainFrame.setObjectName("mainFrame")
        mainFrame.resize(528, 385)
        self.centralwidget = QtWidgets.QWidget(mainFrame)
        self.centralwidget.setObjectName("centralwidget")

        self.lbEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbEmail.setGeometry(QtCore.QRect(50, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbEmail.setFont(font)
        self.lbEmail.setObjectName("lbEmail")

        self.lbSenha = QtWidgets.QLabel(self.centralwidget)
        self.lbSenha.setGeometry(QtCore.QRect(50, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbSenha.setFont(font)
        self.lbSenha.setObjectName("lbSenha")

        self.tfEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.tfEmail.setGeometry(QtCore.QRect(100, 230, 113, 20))
        self.tfEmail.setObjectName("tfEmail")

        self.tfSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.tfSenha.setGeometry(QtCore.QRect(100, 260, 113, 20))
        self.tfSenha.setObjectName("tfSenha")
        self.tfSenha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lcdRelogio = QtWidgets.QLabel(self.centralwidget)
        self.lcdRelogio.setGeometry(QtCore.QRect(410, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdRelogio.setFont(font)
        self.lcdRelogio.setObjectName("lcdRelogio")

        self.btEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btEntrar.setGeometry(QtCore.QRect(150, 290, 61, 29))
        self.btEntrar.setObjectName("btEntrar")
        self.btEntrar.clicked.connect(self.event_logar)

        mainFrame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainFrame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 23))
        self.menubar.setObjectName("menubar")
        self.mnArquivo = QtWidgets.QMenu(self.menubar)
        self.mnArquivo.setObjectName("mnArquivo")
        self.mnSobre = QtWidgets.QMenu(self.menubar)
        self.mnSobre.setObjectName("mnSobre")
        mainFrame.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainFrame)
        self.statusbar.setObjectName("statusbar")
        mainFrame.setStatusBar(self.statusbar)
        self.miAjuda = QtWidgets.QAction(mainFrame)
        self.miAjuda.setObjectName("miAjuda")
        self.miSalvar = QtWidgets.QAction(mainFrame)
        self.miSalvar.setObjectName("miSalvar")
        self.miLimpar = QtWidgets.QAction(mainFrame)
        self.miLimpar.setObjectName("miLimpar")
        self.miCarregar = QtWidgets.QAction(mainFrame)
        self.miCarregar.setObjectName("miCarregar")
        self.mnArquivo.addAction(self.miSalvar)
        self.mnArquivo.addAction(self.miLimpar)
        self.mnArquivo.addAction(self.miCarregar)
        self.mnSobre.addAction(self.miAjuda)
        self.menubar.addAction(self.mnArquivo.menuAction())
        self.menubar.addAction(self.mnSobre.menuAction())

        self.retranslateUi(mainFrame)
        QtCore.QMetaObject.connectSlotsByName(mainFrame)

    def retranslateUi(self, mainFrame):
        _translate = QtCore.QCoreApplication.translate
        mainFrame.setWindowTitle(_translate("mainFrame", "Login"))
        self.lbEmail.setText(_translate("mainFrame", "Email:"))
        self.lbSenha.setText(_translate("mainFrame", "Senha:"))
        self.btEntrar.setText(_translate("mainFrame", "Entrar"))
        self.mnArquivo.setTitle(_translate("mainFrame", "Arquivo"))
        self.mnSobre.setTitle(_translate("mainFrame", "Sobre"))
        self.miAjuda.setText(_translate("mainFrame", "Ajuda"))
        self.miSalvar.setText(_translate("mainFrame", "Salvar"))
        self.miLimpar.setText(_translate("mainFrame", "Limpar"))
        self.miCarregar.setText(_translate("mainFrame", "Carregar"))

    #Eventos:

    def event_logar(self):
        email = self.tfEmail.text()
        password = sha256(self.tfSenha.text().encode('ascii')).hexdigest()

        if isAutenticarLogin(email, password):
            print('Entrou')
            self.exitThread()
        else:
            print('Login/Senha incorreto(s)')
    
    def event_iniciarRelogio(self):
        while(True):
            if self.statusThread == False:
                self.lcdRelogio.clear()
                break

            now = datetime.now()
            
            hora = now.hour
            minuto = now.minute
            segundo = now.second
            sleep(1)
            
            self.lcdRelogio.setText("{} : {} : {}".format(hora, minuto, segundo))

def iniciarTela():
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = QtWidgets.QMainWindow()
    ui = Ui_mainFrame()
    ui.setupUi(mainFrame)
    mainFrame.show()
    app.exec_()
    
    #on close
    ui.exitThread()
    sys.exit()
