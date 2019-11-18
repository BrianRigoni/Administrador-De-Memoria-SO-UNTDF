# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memory_manager_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def browse_files(self):
        print("Browse")

    def start_simulation(self):
        print("Simulate")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_simulate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_simulate.setGeometry(QtCore.QRect(180, 310, 91, 41))
        self.pushButton_simulate.setObjectName("pushButton_simulate")
        ##########################EVENT##################################
        self.pushButton_simulate.clicked.connect(lambda: self.start_simulation())
        self.cbx_strategy = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_strategy.setGeometry(QtCore.QRect(130, 110, 191, 22))
        self.cbx_strategy.setObjectName("cbx_strategy")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(130, 60, 191, 20))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(130, 40, 47, 13))
        self.label_file.setObjectName("label_file")
        self.lineEdit_selection = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_selection.setGeometry(QtCore.QRect(130, 160, 191, 20))
        self.lineEdit_selection.setObjectName("lineEdit_selection")
        self.lineEdit_assignation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_assignation.setGeometry(QtCore.QRect(130, 210, 191, 20))
        self.lineEdit_assignation.setObjectName("lineEdit_assignation")
        self.lineEdit_release = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_release.setGeometry(QtCore.QRect(130, 260, 191, 20))
        self.lineEdit_release.setObjectName("lineEdit_release")
        self.label_strategy = QtWidgets.QLabel(self.centralwidget)
        self.label_strategy.setGeometry(QtCore.QRect(130, 90, 191, 16))
        self.label_strategy.setObjectName("label_strategy")
        self.label_selection = QtWidgets.QLabel(self.centralwidget)
        self.label_selection.setGeometry(QtCore.QRect(130, 140, 191, 16))
        self.label_selection.setObjectName("label_selection")
        self.label_assignation = QtWidgets.QLabel(self.centralwidget)
        self.label_assignation.setGeometry(QtCore.QRect(130, 190, 191, 16))
        self.label_assignation.setObjectName("label_assignation")
        self.label_release = QtWidgets.QLabel(self.centralwidget)
        self.label_release.setGeometry(QtCore.QRect(130, 240, 191, 16))
        self.label_release.setObjectName("label_release")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(330, 60, 75, 21))
        self.pushButton_browse.setObjectName("pushButton_browse")
        ########################CLICKEVENT############################
        self.pushButton_browse.clicked.connect(lambda: self.browse_files())
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador de Memoria - SO - Brian Rigoni "))
        self.pushButton_simulate.setText(_translate("MainWindow", "Simular"))
        self.cbx_strategy.setItemText(0, _translate("MainWindow", "First Fit"))
        self.cbx_strategy.setItemText(1, _translate("MainWindow", "Best Fit"))
        self.cbx_strategy.setItemText(2, _translate("MainWindow", "Worst Fit"))
        self.cbx_strategy.setItemText(3, _translate("MainWindow", "Next Fit"))
        self.label_file.setText(_translate("MainWindow", "Archivo"))
        self.label_strategy.setText(_translate("MainWindow", "Estrategia de Seleccion"))
        self.label_selection.setText(_translate("MainWindow", "Tiempo de Seleccion"))
        self.label_assignation.setText(_translate("MainWindow", "Tiempo de Asignacion"))
        self.label_release.setText(_translate("MainWindow", "Tiempo de Liberacion"))
        self.pushButton_browse.setText(_translate("MainWindow", "Examinar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
