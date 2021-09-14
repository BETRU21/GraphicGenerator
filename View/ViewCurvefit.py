from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5 import QtGui
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}CurvefitWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewCurvefit(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData, modelCurvefit):
        super(ViewCurvefit, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.modelCurvefit = modelCurvefit