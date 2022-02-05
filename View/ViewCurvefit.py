from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import numpy as np
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}CurvefitWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewCurvefit(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData, modelCurvefit):
        super(ViewCurvefit, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.modelCurvefit = modelCurvefit
        self.markerSymbols = ["", ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"]
        self.markerTexts = ["None", "point", "pixel", "circle", "triangle down", "triangle up", "triangle left", "triangle right", "tri down", "tri up", "tri left", "tri right", "octagon", "square", "pentagon", "plus (filled)", "star", "hexagon 1", "hexagon 2", "plus", "x", "x (filled)", "diamond", "thin diamond", "vline", "hline"]
        self.lineStyles = ['solid', 'dashed', 'dashdot', 'dotted']
        self.color = "#48b0b0"
        self.connectWidgets()
        self.setupWidgets()

    def setupWidgets(self): #01
        self.cmb_lineType.clear()
        self.cmb_pos.clear()
        self.cmb_marker.clear()
        self.cmb_function.clear()

        functions = self.modelCurvefit.listFunctions()
        self.cmb_function.addItems(functions)
        self.cmb_lineType.addItems(self.lineStyles)
        self.cmb_marker.addItems(self.markerTexts)
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def connectWidgets(self): #02
        self.cmb_function.currentIndexChanged.connect(self.updateInfo)
        self.cb_p0.stateChanged.connect(self.enableP0)
        self.pb_selectColor.clicked.connect(self.selectColor)
        self.pb_addPlot.clicked.connect(self.plot)
        self.pb_clear.clicked.connect(self.clearData)

    def enableWidgets(self): #03
        self.cmb_function.setEnabled(True)
        self.cmb_pos.setEnabled(True)
        self.cmb_data.setEnabled(True)
        self.pb_selectColor.setEnabled(True)
        self.cmb_lineType.setEnabled(True)
        self.cmb_marker.setEnabled(True)
        self.pb_addPlot.setEnabled(True)
        self.pb_clear.setEnabled(True)
        self.le_popt.setEnabled(True)
        self.le_var.setEnabled(True)
        self.cb_p0.setEnabled(True)

    def enableP0(self): #05
        if self.cb_p0.checkState() == 0:
            self.le_p0.setEnabled(False)
        else:
            self.le_p0.setEnabled(True)

    def updateInfo(self): #06
        key = self.cmb_function.currentText()
        info = self.modelCurvefit.getFunctionForm(key)
        self.le_info.clear()
        self.le_info.setText(info)
        params = self.modelCurvefit.getFunctionParams(key)
        self.la_param.clear()
        self.la_param.setText(params)


    def selectColor(self): #07
        color = QColorDialog.getColor()

        if color.isValid():
            self.color = color.name()
            color = self.color[1:]
            newColor = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            styleSheetParameter = "background-color: rgb" + f"{newColor}"+"; border: 0px;"
            self.pb_selectColor.setStyleSheet(styleSheetParameter)


    def clearData(self): #08
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        self.modelGraphic.deleteSpecificPlot(position)

    def getSelectedData(self): #09
        key = self.cmb_data.currentText()
        data = self.modelData.getData(key)
        dataX = data.get("xValues")
        dataY = data.get("yValues")
        return (dataX, dataY)


    def updateDataList(self, keysList): #10
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)


    def plot(self): #11
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            color = self.color
            marker = self.markerSymbols[self.cmb_marker.currentIndex()]
            lineStyle = self.cmb_lineType.currentText()
            label = self.le_label.text()

            try:
                dataX, dataY = self.getSelectedData()
                key = self.cmb_function.currentText()
                dataX = np.array(dataX)
                dataY = np.array(dataY)
                function = self.modelCurvefit.getFunction(key)
            except Exception as e:
                e = str(e)
                self.consoleView.showOnConsole("There is no data to curvefit. |ERROR:VC#11|", "red")
                raise ValueError("To stop the process after catching the error.")

            try:
                if self.cb_p0.checkState() == 0:
                    curvefit, newDataX = self.modelCurvefit.curvefit(dataX, dataY, function)
                else:
                    p0STR = self.le_p0.text()
                    intermediateList = p0STR.split(",")
                    p0 = list(map(float, intermediateList))   
                    curvefit, newDataX = self.modelCurvefit.curvefit(dataX, dataY, function, P0=p0)
            except Exception as e:
                self.consoleView.showOnConsole("Curvefit failed. |ERROR:VC#11|", "red")
                raise ValueError("To stop the process after catching the error.")

            try:
                self.modelGraphic.addPlot(position, newDataX, curvefit, color, lineStyle, marker, label)
                popt = str(self.modelCurvefit.currentPopt())
                deltaValues = str(self.modelCurvefit.currentDeltaValues())
                self.le_popt.clear()
                self.le_popt.setText(popt)
                self.le_var.clear()
                self.le_var.setText(deltaValues)
                self.consoleView.showOnConsole(f"{self.cmb_function.currentText()} function plot successfully at {self.cmb_pos.currentText()}", "green")
            except Exception as e:
                e = str(e) + " |ERROR:VC#11|"
                self.consoleView.showOnConsole(e, "red")
                raise ValueError("To stop the process after catching the error.")

        except:
            pass # To stop the process after catching the error.
