from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import sys
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}GraphWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewGraph(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData):
        super(ViewGraph, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.markerSymbols = ["", ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"]
        self.markerTexts = ["None", "point", "pixel", "circle", "triangle down", "triangle up", "triangle left", "triangle right", "tri down", "tri up", "tri left", "tri right", "octagon", "square", "pentagon", "plus (filled)", "star", "hexagon 1", "hexagon 2", "plus", "x", "x (filled)", "diamond", "thin diamond", "vline", "hline"]
        self.lineStyles = ["solid", "dashed", "dashdot", "dotted", "None"]
        self.color = "#48b0b0"
        self.colorError = "#000000"
        self.connectWidgets()
        self.setupWidgets()

    def setupWidgets(self): #01
        self.cmb_lineType.clear()
        self.cmb_pos.clear()
        self.cmb_marker.clear()

        self.cmb_lineType.addItems(self.lineStyles)
        self.cmb_marker.addItems(self.markerTexts)
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def connectWidgets(self): #02
        self.pb_addPlot.clicked.connect(self.plot)
        self.pb_dimension.clicked.connect(self.generateGraph)
        self.pb_selectColor.clicked.connect(self.selectColor)
        self.pb_clear.clicked.connect(self.clearData)
        self.pb_selectColorError.clicked.connect(self.selectColorError)
        self.cb_errorBar.stateChanged.connect(self.enableErrorBar)

    def clearData(self): #03
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        self.modelGraphic.deleteSpecificPlot(position)
        self.generateView.deletePlotInfos(position)

    def selectColorError(self): #04
        color = QColorDialog.getColor()

        if color.isValid():
            self.colorError = color.name()
            color = self.colorError[1:]
            newColor = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            styleSheetParameter = "background-color: rgb" + f"{newColor}"+"; border: 0px;"
            self.pb_selectColorError.setStyleSheet(styleSheetParameter)

    def selectColor(self): #04
        color = QColorDialog.getColor()

        if color.isValid():
            self.color = color.name()
            color = self.color[1:]
            newColor = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            styleSheetParameter = "background-color: rgb" + f"{newColor}"+"; border: 0px;"
            self.pb_selectColor.setStyleSheet(styleSheetParameter)

    def generateGraph(self): #05
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
        self.generateView.updateDimensionInfos(x, y)
        self.generateView.resetGraphInfos()

    def enableWidgets(self): #06
        self.cmb_pos.setEnabled(True)
        self.cmb_data.setEnabled(True)
        self.pb_selectColor.setEnabled(True)
        self.cmb_lineType.setEnabled(True)
        self.cmb_marker.setEnabled(True)
        self.pb_addPlot.setEnabled(True)
        self.pb_clear.setEnabled(True)
        self.pb_selectColorError.setEnabled(True)
        self.cb_errorBar.setEnabled(True)
        self.sb_lineThickness.setEnabled(True)

    def getSelectedData(self): #07
        key = self.cmb_data.currentText()
        data = self.modelData.getData(key)
        dataX = data.get("xValues")
        dataY = data.get("yValues")
        return (dataX, dataY)

    def enableErrorBar(self): #05
        if self.cb_errorBar.checkState() == 0:
            self.sb_Xerror.setEnabled(False)
            self.sb_Yerror.setEnabled(False)
            self.sb_errorThickness.setEnabled(False)
            self.sb_errorBarSize.setEnabled(False)
            self.cmb_errorType.setEnabled(False)
            # Finir ensuite
        else:
            self.sb_Xerror.setEnabled(True)
            self.sb_Yerror.setEnabled(True)
            self.sb_errorThickness.setEnabled(True)
            self.sb_errorBarSize.setEnabled(True)
            self.cmb_errorType.setEnabled(True)

    def plot(self): #08
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            try:
                dataName = self.cmb_data.currentText()
                dataX, dataY = self.getSelectedData()
                color = self.color
                errorBarColor = self.colorError
                marker = self.markerSymbols[self.cmb_marker.currentIndex()]
                lineStyle = self.cmb_lineType.currentText()
                label = self.cmb_data.currentText()
                xError = float(self.sb_Xerror.value())
                yError = float(self.sb_Yerror.value())
                errorBarSize = self.sb_errorBarSize.value()
                errorBarThickness = self.sb_errorThickness.value()
                linewidth = self.sb_lineThickness.value()

                # faire ici
            except Exception as e:
                self.consoleView.showOnConsole("There is no data to plot. |ERROR:VG#08|", "red")
                raise ValueError("To stop the process after catching the error.")
            try:
                if self.cb_errorBar.checkState() == 2:
                    if self.cmb_errorType.currentIndex() == 0:
                        self.modelGraphic.addPlot(position, dataX, dataY, color, lineStyle, marker, label, errorBarX=xError, errorBarY=yError, Ecolor=errorBarColor, errorSize=errorBarSize, errorThickness=errorBarThickness, lineWidth=linewidth)
                        self.generateView.addPlotInfos(position, dataName, color, lineStyle, marker, label, errorBarX=xError, errorBarY=yError, Ecolor=errorBarColor, errorSize=errorBarSize, errorThickness=errorBarThickness, lineWidth=linewidth)
                    else:
                        self.modelGraphic.addPlot(position, dataX, dataY, color, lineStyle, marker, label, errorBarX=xError, errorBarY=yError, Ecolor=errorBarColor, errorSize=errorBarSize, errorThickness=errorBarThickness, percentage=True, lineWidth=linewidth)
                        self.generateView.addPlotInfos(position, dataName, color, lineStyle, marker, label, errorBarX=xError, errorBarY=yError, Ecolor=errorBarColor, errorSize=errorBarSize, errorThickness=errorBarThickness, percentage=True, lineWidth=linewidth)
                else:
                    self.modelGraphic.addPlot(position, dataX, dataY, color, lineStyle, marker, label, lineWidth=linewidth)
                    self.generateView.addPlotInfos(position, dataName, color, lineStyle, marker, label, lineWidth=linewidth)
            except Exception as e:
                e = str(e) + " |ERROR:VG#08|"
                self.consoleView.showOnConsole(e, "red")
                raise ValueError("To stop the process after catching the error.")
            self.consoleView.showOnConsole(f"{self.cmb_data.currentText()} plot successfully at {self.cmb_pos.currentText()}", "green")
        except:
            pass# To stop the process after catching the error.

    def updateDataList(self, keysList): #09
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)
