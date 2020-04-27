# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orcamento.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        self.menuOrcamento = QtWidgets.QMenu(self.menubar)
        self.menuOrcamento.setObjectName("menuOrcamento")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo = QtWidgets.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.menuOrcamento.addAction(self.actionNovo)
        self.menuOrcamento.addAction(self.actionSalvar)
        self.menuOrcamento.addAction(self.actionImprimir)
        self.menubar.addAction(self.menuOrcamento.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOrcamento.setTitle(_translate("MainWindow", "Orçamentos"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.actionNovo.setText(_translate("MainWindow", "Novo"))
        self.actionNovo.setStatusTip(_translate("MainWindow", "Cria um novo orçamento"))
        self.actionNovo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setStatusTip(_translate("MainWindow", "Salva o orçamento"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.actionImprimir.setShortcut(_translate("MainWindow", "Ctrl+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
