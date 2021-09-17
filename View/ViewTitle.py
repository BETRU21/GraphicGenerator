from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import sys
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}TitleWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

# TODO : Faire les fonctionnalités de légendes et titres.

class ViewTitle(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData):
        super(ViewTitle, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData

