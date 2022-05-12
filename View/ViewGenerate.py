from Model.GenerateCode import generate
from typing import NamedTuple, Any
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}GenerateWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class Data(NamedTuple):
    path: str = None
    splitSymbol: str = None
    deleteFirstRow: int = 0
    xValuesColumn: int = 0
    yValuesColumn: int = 1
    normaliseX: bool = False
    normaliseY: bool = False

class Dimension(NamedTuple):
    col: int = None
    row: int = None

class Plot(NamedTuple):
    dataName: str = None
    Color: str = None
    lineStyle: str = None
    Marker: str = None
    Label: str = None
    errorBarX: Any = None
    errorBarY: Any = None
    Ecolor: str = None
    errorSize: int = None
    errorThickness: int = None
    percentage: bool = None
    lineWidth: int = None

class Fit(NamedTuple):
    function: str = None
    ID: str = None
    data: str = None

class Params(NamedTuple):
    ID: str = None
    p0: list = None

class Text(NamedTuple):
    text: str = None
    fontSize: int = None

class ViewGenerate(QWidget, Ui_MainWindow):
    def __init__(self):
        super(ViewGenerate, self).__init__()
        self.setupUi(self)
        self.connectWidgets()
        self.datas = {}
        self.dimension = Dimension(1,1)
        self.plots = {}
        self.curvefits = {}
        self.p0s = []
        self.ID = 0
        self.legends = {}
        self.title = Text("", 12)
        self.xSubtitles = {}
        self.ySubtitles = {}

    def connectWidgets(self): #02
        self.pb_generate.clicked.connect(self.generateCode)

    def addLegend(self, position, fonSize):
        self.legends[str(position)] = fontSize

    def addLegends(self, fontSize):
        self.legends = {}
        x = self.dimension.col
        y = self.dimension.row
        for i in range(x):
            for j in range(y):
                self.legends[f"({i+1}, {j+1})"] = fontSize

    def deleteLegend(self, position):
        self.legends.pop(str(position))

    def deleteLegends(self):
        self.legends = {}

    def addSubtitle(self, position, subtitle, fontSize):
        pass

    def addTitle(self, title, fontSize):
        self.title = Text(title, fontSize)

    def addXSubtitle(self,position, subtitle, fontSize):
        self.xSubtitles[str(position)] = Text(subtitle, fontSize)

    def addYSubtitle(self,position, subtitle, fontSize):
        self.ySubtitles[str(position)] = Text(subtitle, fontSize)

    def addDataInfos(self, path, dataName, splitSymbol, deleteFirstRow, xValuesColumn, yValuesColumn, normaliseX, normaliseY):
        if str(dataName) in list(self.datas.keys()):
            pass
        else:
            self.datas[str(dataName)] = Data(path, splitSymbol, deleteFirstRow, xValuesColumn, yValuesColumn, normaliseX, normaliseY)

    def deleteDataInfos(self, dataName):
        try:
            self.datas.pop(dataName)
        except:
            pass
    def resetDataInfos(self):
        self.datas = {}

    def addPlotInfos(self, position, dataName, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):
        if str(position) in list(self.plots.keys()):
            self.plots[str(position)].append(Plot(dataName, Color, lineStyle, Marker, Label, errorBarX, errorBarY, Ecolor, errorSize, errorThickness, percentage, lineWidth))
        else:
            self.plots[str(position)] = [Plot(dataName, Color, lineStyle, Marker, Label, errorBarX, errorBarY, Ecolor, errorSize, errorThickness, percentage, lineWidth)]

    def updateDimensionInfos(self, col, row):
        self.dimension = Dimension(col, row)

    def deletePlotInfos(self, position):
        try:
            self.plots.pop(str(position))
            self.curvefits.pop(str(position))
        except:
            pass

    def addCurvefitInfos(self, position, dataName, function, p0, Color, lineStyle, Marker, Label, lineWidth):
        self.ID += 1
        ID = "curvefit" + str(self.ID)
        if str(position) in list(self.curvefits.keys()):
            self.curvefits[str(position)].append(Fit(function, ID, dataName))
        else:
            self.curvefits[str(position)] = [Fit(function, ID, dataName)]

        self.p0s.append(Params(ID, p0))

        if str(position) in list(self.plots.keys()):
            self.plots[str(position)].append(Plot(ID, Color, lineStyle, Marker, Label, None, None, "#000000", None, None, False, lineWidth))
        else:
            self.plots[str(position)] = [Plot(ID, Color, lineStyle, Marker, Label, None, None, "#000000", None, None, False, lineWidth)]

    def resetGraphInfos(self):
        self.plots = {}
        self.curvefits = {}
        self.p0s = []

    def generateCode(self):
        if self.le_name.text() == "":
            self.consoleView.showOnConsole("The file has no name", "red")
        else:
            functions, fits, p0s = self.clearCurvefitInfos()
            try:
                self.printInfos()
                generate(self.le_name.text(), self.datas, self.dimension, self.plots, functions, fits, p0s, self.legends, self.title, self.xSubtitles, self.ySubtitles)
            except Exception as e:
                e = str(e)
                print(e)
                self.consoleView.showOnConsole(e, "red")

    def clearCurvefitInfos(self):
        functions = []
        validID = []
        fits = []
        for pos in list(self.curvefits.keys()):
            for fit in (self.curvefits.get(pos)):
                if not fit.function in functions:
                    functions.append(fit.function)
                    validID.append(fit.ID)
                    fits.append(fit)
        p0s = {}
        for ID in validID:
            for params in self.p0s:
                if ID == params.ID:
                    if params.p0 != "None":
                        p0s[params.ID] = params.p0
        return functions, fits, p0s

    def printInfos(self):
        print(self.datas)
        print("----------------------------------------------------------")
        print(self.dimension)
        print("----------------------------------------------------------")
        print(self.plots)
        print("----------------------------------------------------------")
        print(self.curvefits)
        print("----------------------------------------------------------")
        print(self.p0s)
        print("----------------------------------------------------------")
        print(self.ID)
        print("----------------------------------------------------------")
        print(self.legends)
        print("----------------------------------------------------------")
        print(self.title)
        print("----------------------------------------------------------")
        print(self.xSubtitles)
        print("----------------------------------------------------------")
        print(self.ySubtitles)
        print("----------------------------------------------------------")
