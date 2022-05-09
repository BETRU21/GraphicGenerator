#from Model.GenerateCode import generate
from typing import NamedTuple
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}GenerateWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class Data(NamedTuple):
    path: str = None
    splitSymbol: str = None
    deleteFirstRow: int = None
    xValuesColumn: int = None
    yValuesColumn: int = None
    normaliseX: bool = False
    normaliseY: bool = False

class Dimension(NamedTuple):
    row: int = None
    line: int = None

class ViewGenerate(QWidget, Ui_MainWindow):
    def __init__(self):
        super(ViewGenerate, self).__init__()
        self.setupUi(self)
        self.datas = {}
        self.dimension = Dimension(1,1)

    def addDataInfos(self, path, dataName, splitSymbol, deleteFirstRow, xValuesColumn, yValuesColumn, normaliseX, normaliseY):
        if str(dataName) in list(self.datas.keys()):
            pass
        else:
            self.datas[str(dataName)] = Data(path, splitSymbol, deleteFirstRow, xValuesColumn, yValuesColumn, normaliseX, normaliseY)

    def deleteDataInfos(self, dataName):
        self.datas.pop(dataName)
    def resetDataInfos(self):
        self.datas = {}

    def addPlotInfos(self, position, dataName, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):
        print("addPlot")

    def updateDimensionInfos(self, row, line):
        self.dimension = Dimension(row, line)

    def deletePlotInfos(self, position):
        print("resetPlot")

    def addCurvefitInfos(self, position, dataName, function, p0, color, lineStyle, marker, label):
        print("addCurvefit")
