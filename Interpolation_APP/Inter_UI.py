# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inter_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagePath = QtWidgets.QTextEdit(self.centralwidget)
        self.imagePath.setEnabled(True)
        self.imagePath.setGeometry(QtCore.QRect(20, 30, 531, 31))
        self.imagePath.setObjectName("imagePath")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(560, 30, 91, 31))
        self.open.setObjectName("open")
        self.ori = QtWidgets.QLabel(self.centralwidget)
        self.ori.setGeometry(QtCore.QRect(20, 120, 511, 491))
        self.ori.setFrameShape(QtWidgets.QFrame.Box)
        self.ori.setText("")
        self.ori.setScaledContents(True)
        self.ori.setObjectName("ori")
        self.modelPath = QtWidgets.QComboBox(self.centralwidget)
        self.modelPath.setGeometry(QtCore.QRect(20, 70, 531, 31))
        self.modelPath.setObjectName("modelPath")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.modelPath.addItem("")
        self.use_cuda = QtWidgets.QCheckBox(self.centralwidget)
        self.use_cuda.setGeometry(QtCore.QRect(560, 120, 131, 21))
        self.use_cuda.setChecked(True)
        self.use_cuda.setObjectName("use_cuda")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(560, 260, 91, 31))
        self.save.setObjectName("save")
        self.auto_save = QtWidgets.QCheckBox(self.centralwidget)
        self.auto_save.setGeometry(QtCore.QRect(560, 300, 101, 21))
        self.auto_save.setObjectName("auto_save")
        self.save_option = QtWidgets.QComboBox(self.centralwidget)
        self.save_option.setGeometry(QtCore.QRect(550, 210, 111, 31))
        self.save_option.setObjectName("save_option")
        self.save_option.addItem("")
        self.save_option.addItem("")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(560, 70, 91, 31))
        self.load.setObjectName("load")
        self.revert = QtWidgets.QPushButton(self.centralwidget)
        self.revert.setGeometry(QtCore.QRect(560, 160, 91, 31))
        self.revert.setObjectName("revert")
        self.imagePath.raise_()
        self.open.raise_()
        self.ori.raise_()
        self.save.raise_()
        self.modelPath.raise_()
        self.auto_save.raise_()
        self.revert.raise_()
        self.load.raise_()
        self.use_cuda.raise_()
        self.save_option.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interpolation"))
        self.open.setText(_translate("MainWindow", "OPEN"))
        self.modelPath.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.modelPath.setItemText(0, _translate("MainWindow", "denoise&bgremoval2x"))
        self.modelPath.setItemText(1, _translate("MainWindow", "denoise2x"))
        self.modelPath.setItemText(2, _translate("MainWindow", "dataset_interpolation4x"))
        self.use_cuda.setText(_translate("MainWindow", "Use CUDA"))
        self.save.setText(_translate("MainWindow", "SAVE"))
        self.auto_save.setText(_translate("MainWindow", "Auto Save"))
        self.save_option.setItemText(0, _translate("MainWindow", "Save ALL"))
        self.save_option.setItemText(1, _translate("MainWindow", "Model output"))
        self.load.setText(_translate("MainWindow", "LOAD"))
        self.revert.setText(_translate("MainWindow", "REVERT"))

