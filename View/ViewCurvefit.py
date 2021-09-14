from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import uic
import numpy as np
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}CurvefitWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

# TODO : Connecter tout les widgets et mettre les fonctionnalités

class ViewCurvefit(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData, modelCurvefit):
        super(ViewCurvefit, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.modelCurvefit = modelCurvefit

    def test(self):
        dataX = np.array([1,2,3,4,5,6,7,8,9])
        dataY = np.array([0,2,4,6,8,10,12,14,16])

        f = modelCurvefit.getFunction("straightLine")

        line, popt = modelCurvefit.curvefit(dataX, dataY, f)

        print(popt)
        print(modelCurvefit.getFunctionParam("straightLine"))
