from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import uic
import numpy as np
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}ModifyDataWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewModifyData(QWidget, Ui_MainWindow):
    def __init__(self, modelData):
        super(ViewModifyData, self).__init__()
        self.setupUi(self)
        self.modelData = modelData
        self.connectWidgets()

    def getSelectedData(self): #07
        key = self.cmb_data.currentText()
        data = self.modelData.getData(key)
        dataX = data.get("xValues")
        dataY = data.get("yValues")
        return (dataX, dataY)

    def connectWidgets(self): #02
        self.cmb_data.currentIndexChanged.connect(self.preview)
        self.pb_apply.clicked.connect(self.applyChangeOnData)

    def applyChangeOnData(self): #06
        dataName = self.le_dataName.text()
        dataX, dataY = self.getSelectedData()
        try:
            if self.cb_normaliseX.checkState() == 2:
                dataX = np.array(dataX)
                dataX = dataY/max(dataX)
            if self.cb_normaliseY.checkState() == 2:
                dataY = np.array(dataY)
                dataY = dataY/max(dataY)
            self.modelData.dataDict[dataName] = {"xValues": dataX, "yValues": dataY}
            self.updateDataLoaded()
            self.consoleView.showOnConsole("Successfully extracted data!", "green")
        except Exception as e:
            e = str(e) + " |ERROR:VD#06|"
            self.consoleView.showOnConsole(e, "red")

    def updateDataLoaded(self): #07
        keysList = self.modelData.listData()
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)
        self.graphView.updateDataList(keysList)
        self.curvefitView.updateDataList(keysList)
        lastIndice = self.cmb_data.count() - 1
        self.cmb_data.setCurrentIndex(lastIndice)

        self.dataView.cmb_data.clear()
        self.dataView.cmb_data.addItems(keysList)

    def preview(self): #10
        try:
            key = self.cmb_data.currentText()
            data = self.modelData.getData(key)
            xValues = data.get("xValues")
            yValues = data.get("yValues")
            if len(xValues) > 50:
                xValues = xValues[:50]
                yValues = yValues[:50]
            preview = [" xValues | yValues"]
            for i, item in enumerate(xValues):
                line = str(item) + " | " + str(yValues[i])
                preview.append(line)
            self.lw_preview.clear()
            self.lw_preview.addItems(preview)
        except:
            self.lw_preview.clear()
