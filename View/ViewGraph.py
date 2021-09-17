from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import sys
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}GraphWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

# TODO : Faire les fonctionnalités de légendes et titres.

class ViewGraph(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData):
        super(ViewGraph, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.markerSymbols = ["", ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"]
        self.markerTexts = ["None", "point", "pixel", "circle", "triangle down", "triangle up", "triangle left", "triangle right", "tri down", "tri up", "tri left", "tri right", "octagon", "square", "pentagon", "plus (filled)", "star", "hexagon 1", "hexagon 2", "plus", "x", "x (filled)", "diamond", "thin diamond", "vline", "hline"]
        self.lineStyles = ['solid', 'dashed', 'dashdot', 'dotted']
        self.color = "#48b0b0"
        self.connectWidgets()
        self.setupWidgets()

    def setupWidgets(self):
        self.cmb_lineType.clear()
        self.cmb_pos.clear()
        self.cmb_marker.clear()

        self.cmb_lineType.addItems(self.lineStyles)
        self.cmb_marker.addItems(self.markerTexts)
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def connectWidgets(self):
        self.pb_addPlot.clicked.connect(self.plot)
        self.pb_dimension.clicked.connect(self.generateGraph)
        self.pb_selectColor.clicked.connect(self.selectColor)
        self.pb_clear.clicked.connect(self.clearData)

    def clearData(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        self.modelGraphic.deleteSpecificPlot(position)

    def selectColor(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color = color.name()
            color = self.color[1:]
            newColor = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            styleSheetParameter = "QCheckBox::indicator{background-color: rgb" + f"{newColor}"+";}"
            self.ind_color.setStyleSheet(styleSheetParameter)

    def generateGraph(self):
        x = self.sb_x.value()
        y = self.sb_y.value()
        self.modelGraphic.generateGraph(x, y)
        self.consoleView.showOnConsole(f"A new graphic {x}x{y} has been successfully created!", "green")
        self.setupWidgets()
        self.curvefitView.setupWidgets()
        self.titleView.setupWidgets()
        self.enableWidgets()
        self.curvefitView.enableWidgets()
        self.titleView.enableWidgets()

    def enableWidgets(self):
        self.cmb_pos.setEnabled(True)
        self.cmb_data.setEnabled(True)
        self.pb_selectColor.setEnabled(True)
        self.cmb_lineType.setEnabled(True)
        self.cmb_marker.setEnabled(True)
        self.pb_addPlot.setEnabled(True)
        self.pb_clear.setEnabled(True)

    def getSelectedData(self):
        key = self.cmb_data.currentText()
        data = self.modelData.getData(key)
        dataX = data.get("xValues")
        dataY = data.get("yValues")
        return (dataX, dataY)

    def plot(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        dataX, dataY = self.getSelectedData()
        color = self.color
        marker = self.markerSymbols[self.cmb_marker.currentIndex()]
        lineStyle = self.cmb_lineType.currentText()
        try:
            self.modelGraphic.addPlot(position, dataX, dataY, color, lineStyle, marker)
        except Exception as e:
            e = str(e)
            self.consoleView.showOnConsole(e, "red")
        self.consoleView.showOnConsole(f"{self.cmb_data.currentText()} plot successfully at {self.cmb_pos.currentText()}", "green")

    def updateDataList(self, keysList):
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)
