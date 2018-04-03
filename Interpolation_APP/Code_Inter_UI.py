#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# NOTIFICATION
# The model used in this applicaiton is from
# https://github.com/pytorch/examples/tree/master/super_resolution

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from Inter_UI import Ui_MainWindow
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
import torch
import os
from os.path import exists, join
from torchvision.transforms import ToTensor
from torch.autograd import Variable
import numpy as np
import torchvision
from skimage.morphology import opening, watershed, disk, erosion
from skimage.feature import canny
from scipy import ndimage as ndi
from skimage.filters import sobel
from skimage.measure import regionprops
from skimage.draw import set_color
from utils import load_model, PIL2Pixmap, map01




class Code_MainWindow(Ui_MainWindow):
    def __init__(self, parent = None):
        super(Code_MainWindow, self).__init__()

        self.setupUi(self)
        self.open.clicked.connect(self.BrowseFolder)
        self.load.clicked.connect(self.LoadModel)

        self.revert.clicked.connect(self.RevertAll)

        self.save.clicked.connect(self.Save)

        self.__curdir = os.getcwd() #current directory

        self.ori_content = None  #original image, PIL format
        self.output_image = None #output image of model, PIL format

        self.model_output_content = None
        self.model_output = None

        self.__models = {
                'denoise&bgremoval2x' : 2,
                'denoise2x' : 2,
                'dataset_interpolation4x' : 4,
                'Model 4' : 4,
                'Model 5' : 5,
                'Model 6' : 6
        }


    def BrowseFolder(self):
        self.imagePath_content, _ = QFileDialog.getOpenFileName(self,
                                                            "open",
                                                            "/home/",
                                                            "All Files (*);; Image Files (*.png *.tif *.jpg)")
        if self.imagePath_content:
            self.imagePath.setText(self.imagePath_content)
            self.ori_content = Image.open(self.imagePath_content).convert('L')
            self.height, self.width = self.ori_content.size
            pix_image = PIL2Pixmap(self.ori_content)
            self.ori.setPixmap(pix_image)
            self.ori.show()

    def __load_model(self):
        if not self.ori_content:
            raise Exception("No image is selected.")
        self.cuda = self.use_cuda.isChecked()
        if os.name == 'posix':
            model_path = self.__curdir + '/' + self.modelPath_content + '.pth'
        else:
            model_path = self.__curdir + '\\' + self.modelPath_content + '.pth'

        result = load_model(model_path, self.ori_content, self.scale_factor, self.cuda)

        self.model_output_content = map01(result)
        self.model_output_content = (self.model_output_content * 255 / np.max(self.model_output_content)).astype('uint8')
        self.output_image = Image.fromarray((self.model_output_content), mode = 'L')
        pix_image = PIL2Pixmap(self.output_image)

        self.model_output.resize(QtCore.QSize(self.model_output_content.shape[0],self.model_output_content.shape[1]))
        self.model_output.setPixmap(pix_image)
        self.model_output.show()
        del result # free memory caused by temporary matrix-result

    def LoadModel(self):

        self.modelPath_content = self.modelPath.currentText()
        self.scale_factor = self.__models[self.modelPath_content]

        self.model_output = QtWidgets.QLabel("Output")
        self.model_output.setScaledContents(True)
        self.__load_model()



    def RevertAll(self):
        if self.model_output:
            self.model_output.clear()
        del self.model_output

    def GetSavePath(self):

        file_name = self.imagePath_content.split('/')[-1]
        suffix = '.' + file_name.split('.')[-1]
        name_no_suffix = file_name.replace(suffix, '')
        has_content = True

        if self.auto_save.isChecked():
            if os.name == 'posix':
                save_path = self.__curdir + '/' + name_no_suffix
            else:
                save_path = self.__curdir + '\\' + name_no_suffix
        else:
            if os.name == 'posix':
                path = QFileDialog.getExistingDirectory(self, "save", "/home",
                                                            QFileDialog.ShowDirsOnly
                                                            | QFileDialog.DontResolveSymlinks)
                if not path:
                    has_content = False

                save_path = path + '/' + name_no_suffix
            else:
                path = QFileDialog.getExistingDirectory(self, "save", self.__curdir,
                                                        QFileDialog.ShowDirsOnly
                                                        | QFileDialog.DontResolveSymlinks)
                if not path:
                    has_content = False
                save_path = path + '\\' + name_no_suffix

        if has_content:
            if not exists(save_path):
                os.mkdir(save_path)

            if os.name == 'posix':
                temp_path = save_path + '/' + name_no_suffix
            else:
                temp_path = save_path + '\\' + name_no_suffix
        else:
            temp_path = None

        return temp_path, suffix

    def Save(self):
        opt = self.save_option.currentText()
        _path, suffix = self.GetSavePath()

        if  not _path:
            return

        if opt == 'Model output':
            new_save_name = _path + '_output_' + self.modelPath_content + suffix
            self.output_image.save(new_save_name)


        if opt == 'Save ALL':
            new_save_name = _path + '_output_' + self.modelPath_content + suffix
            self.output_image.save(new_save_name)
            new_save_name = _path + '_2panel_' + self.modelPath_content + suffix
            width, height = self.output_image.size
            two_panel_image = Image.new('L', (width, height * 2 + 1))
            two_panel_image.paste(self.ori_content, (0,0))
            two_panel_image.paste(self.output_image, (0, height + 1))
            two_panel_image.save(new_save_name)
            del two_panel_image


    def release(self):
        if self.model_output:
            self.model_output.clear()
        self.ori.clear()
        del self.output_image

        return


    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                            "Confirm Exit...",
                                            "Are you sure you want to exit?",
                                            QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            self.release()
            event.accept()


qtCreatorFile = "Inter_UI.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Code_MainWindow()
    window.show()
    sys.exit(app.exec_())
