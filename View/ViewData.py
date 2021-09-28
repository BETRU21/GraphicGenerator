from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}DataWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewData(QWidget, Ui_MainWindow):
    def __init__(self, modelData):
        super(ViewData, self).__init__()
        self.setupUi(self)
        self.modelData = modelData
        self.setupWidgets()
        self.connectWidgets()

    def setupWidgets(self): #01
        self.cmb_split.addItems([",", ";", ":", ".", ""])

    def connectWidgets(self): #02
        self.pb_filePath.clicked.connect(self.setFilePath)
        self.le_dataName.textChanged.connect(self.changeDataNameColorIndicator)
        self.pb_extract.clicked.connect(self.extractData)
        self.pb_reset.clicked.connect(self.resetData)
        self.cmb_data.currentIndexChanged.connect(self.preview)
        self.sb_nbColumns.valueChanged.connect(self.setMaxColumn)

    def setMaxColumn(self): #03
        maximum = self.sb_nbColumns.value()
        self.sb_xValues.setMaximum(maximum)
        self.sb_yValues.setMaximum(maximum)

    def changeDataNameColorIndicator(self): #04
        self.ind_dataName.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.pb_extract.setEnabled(True)

    def changeFilePathColorIndicator(self, color): #05
        if color == "green":
            indColor = "QCheckBox::indicator{background-color: rgb(0,255,0);}"
        elif color == "orange":
            indColor = "QCheckBox::indicator{background-color: rgb(255,136,0);}"
        elif color == "red":
            indColor = "QCheckBox::indicator{background-color: rgb(255,0,0);}" 
        else:
            raise ValueError("This color is not valid.")
        self.ind_filePath.setStyleSheet(indColor)

    def extractData(self): #06
        path = self.le_filePath.text()
        dataName = self.le_dataName.text()
        splitSymbol = self.cmb_split.currentText()
        deleteFirstRow = self.sb_row.value()
        xValuesColumn = self.sb_xValues.value() - 1
        yValuesColumn = self.sb_yValues.value() - 1
        try:
            self.modelData.addData(path, dataName, splitSymbol, deleteFirstRow, xValuesColumn, yValuesColumn)
            self.updateDataLoaded()
            self.pb_extract.setEnabled(False)
            self.changeFilePathColorIndicator("orange")
            self.ind_dataName.setStyleSheet("QCheckBox::indicator{background-color: rgb(255,0,0);}")
            self.pb_reset.setEnabled(True)
            self.consoleView.showOnConsole("Successfully extracted data!", "green")
        except Exception as e:
            e = str(e) + " |ERROR:VD#06|"
            self.consoleView.showOnConsole(e, "red")

    def updateDataLoaded(self): #07
        keysList = self.modelData.dataDict.keys()
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)
        self.graphView.updateDataList(keysList)
        self.curvefitView.updateDataList(keysList)
        lastIndice = self.cmb_data.count() - 1
        self.cmb_data.setCurrentIndex(lastIndice)

    def setFilePath(self): #08
        try:
            filePath = QFileDialog.getOpenFileName(self, "Select File")[0]
            if filePath == "":
                raise ValueError("filePath is empty.")
            self.le_filePath.setText(filePath)
            self.consoleView.showOnConsole("filePath found !", "green")
            self.changeFilePathColorIndicator("green")
        except Exception as e:
            e = str(e) + " |ERROR:VD#08|"
            self.consoleView.showOnConsole(e, "red")
            self.changeFilePathColorIndicator("red")

    def resetData(self): #09
        self.cmb_data.clear()
        self.graphView.cmb_data.clear()
        self.modelData.resetDataDict()
        self.ind_dataName.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.ind_filePath.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.pb_extract.setEnabled(True)

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
