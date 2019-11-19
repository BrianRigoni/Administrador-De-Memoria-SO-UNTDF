# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memory_manager_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from models import BestFit, NextFit, FirstFit, WorstFit, MemoryManager, Task


class Ui_MainWindow(object):

    def browse_files(self):
        # Cargo el dialog para buscar archivos
        root = tk.Tk() 
        root.withdraw()
        file_path = filedialog.askopenfilename()
        # Muestro la ruta del archivo en el formulario
        self.lineEdit_file.setText(file_path)

    def get_strategy(self):
        if self.cbx_strategy.currentText() == 'First Fit':
            return FirstFit()
        elif self.cbx_strategy.currentText() == 'Best Fit':
            return BestFit()
        elif self.cbx_strategy.currentText() == 'Worst Fit':
            return WorstFit()
        elif self.cbx_strategy.currentText() == 'Next Fit':
            return NextFit()


    # PARA CARGA DE DATASET
    # Obtiene el contenido de un archivo

    def get_file_contents(self, file_path):
        file = open(file_path, "r")
        contents = file.readlines()
        file.close()
        return contents


    # En base al archivo leido, instancia las tareas
    def fill_tasks(self, data):
        print("-------------CARGANDO DATASET-------------")
        tasks = []
        for line in data:
            splitted_values = line.split(',')
            task_name = splitted_values[0]
            task_space = splitted_values[1]
            task_time = splitted_values[2]
            task = Task(name=task_name, space_requested=task_space, time_requested=task_time)
            tasks.append(task)
            print(task)
        return tasks

    def start_simulation(self):
        # Necesario para instanciar
        file_contents = self.get_file_contents(self.lineEdit_file.text())
        tasks = self.fill_tasks(file_contents) 
        strategy = self.get_strategy()
        selection_time = int(self.lineEdit_selection.text())
        assignation_time = int(self.lineEdit_assignation.text())
        release_time = int(self.lineEdit_release.text())
        memory_qty = int(self.lineEdit_memoryqty.text())
        memory_manager = MemoryManager(selection_algorithm=strategy, tasks=tasks, memory_qty=memory_qty, selection_time=selection_time, assignation_time=assignation_time, release_time=release_time)
        memory_manager.execute_tasks()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_simulate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_simulate.setGeometry(QtCore.QRect(180, 330, 91, 21))
        self.pushButton_simulate.setObjectName("pushButton_simulate")
        ##########################EVENT##################################
        self.pushButton_simulate.clicked.connect(lambda: self.start_simulation())
        self.cbx_strategy = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_strategy.setGeometry(QtCore.QRect(130, 90, 191, 22))
        self.cbx_strategy.setObjectName("cbx_strategy")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.cbx_strategy.addItem("")
        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(130, 40, 191, 20))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(130, 20, 47, 13))
        self.label_file.setObjectName("label_file")
        self.lineEdit_selection = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_selection.setGeometry(QtCore.QRect(130, 140, 191, 20))
        self.lineEdit_selection.setObjectName("lineEdit_selection")
        self.lineEdit_assignation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_assignation.setGeometry(QtCore.QRect(130, 190, 191, 20))
        self.lineEdit_assignation.setObjectName("lineEdit_assignation")
        self.lineEdit_release = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_release.setGeometry(QtCore.QRect(130, 240, 191, 20))
        self.lineEdit_release.setObjectName("lineEdit_release")
        self.label_strategy = QtWidgets.QLabel(self.centralwidget)
        self.label_strategy.setGeometry(QtCore.QRect(130, 70, 191, 16))
        self.label_strategy.setObjectName("label_strategy")
        self.label_selection = QtWidgets.QLabel(self.centralwidget)
        self.label_selection.setGeometry(QtCore.QRect(130, 120, 191, 16))
        self.label_selection.setObjectName("label_selection")
        self.label_assignation = QtWidgets.QLabel(self.centralwidget)
        self.label_assignation.setGeometry(QtCore.QRect(130, 170, 191, 16))
        self.label_assignation.setObjectName("label_assignation")
        self.label_release = QtWidgets.QLabel(self.centralwidget)
        self.label_release.setGeometry(QtCore.QRect(130, 220, 191, 16))
        self.label_release.setObjectName("label_release")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(330, 40, 75, 21))
        self.pushButton_browse.setObjectName("pushButton_browse")
        ########################CLICKEVENT############################
        self.pushButton_browse.clicked.connect(lambda: self.browse_files())
        self.lineEdit_memoryqty = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_memoryqty.setGeometry(QtCore.QRect(130, 290, 191, 20))
        self.lineEdit_memoryqty.setObjectName("lineEdit_memoryqty")
        self.label_memoryqty = QtWidgets.QLabel(self.centralwidget)
        self.label_memoryqty.setGeometry(QtCore.QRect(130, 270, 191, 16))
        self.label_memoryqty.setObjectName("label_memoryqty")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Administrador de Memoria - SO - Brian Rigoni"))
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
        self.label_memoryqty.setText(_translate("MainWindow", "Tamaño de Memoria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
