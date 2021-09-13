from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}DataWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

applicationPath = os.path.abspath("")

class ViewData(QWidget, Ui_MainWindow):
    def __init__(self, modelData):
        super(ViewData, self).__init__()
        self.setupUi(self)
        self.modelData = modelData
        self.appControl = None
        self.setupWidgets()
        self.connectWidgets()

    def setupWidgets(self):
        self.cmb_split.addItems([",", ";", ":", ".", ""])

    def connectWidgets(self):
        self.pb_filePath.clicked.connect(self.setFilePath)
        self.le_dataName.textChanged.connect(self.changeDataNameColorIndicator)
        self.pb_extract.clicked.connect(self.extractData)
        self.pb_reset.clicked.connect(self.resetData)
        self.cmb_data.currentIndexChanged.connect(self.preview)
        self.sb_nbColumns.valueChanged.connect(self.setMaxColumn)

    def setMaxColumn(self):
        maximum = self.sb_nbColumns.value()
        self.sb_xValues.setMaximum(maximum)
        self.sb_yValues.setMaximum(maximum)

    def changeDataNameColorIndicator(self):
        self.ind_dataName.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.pb_extract.setEnabled(True)

    def changeFilePathColorIndicator(self, color):
        if color == "green":
            indColor = "QCheckBox::indicator{background-color: rgb(0,255,0);}"
        elif color == "orange":
            indColor = "QCheckBox::indicator{background-color: rgb(255,136,0);}"
        else:
            raise ValueError("This color is not valid.")
        self.ind_filePath.setStyleSheet(indColor)

    def extractData(self):
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
            self.appControl.showOnConsole("Successfully extracted data!", "green")
        except Exception as e:
            e = str(e)
            self.appControl.showOnConsole(e, "red")

    def updateDataLoaded(self):
        keysList = self.modelData.dataDict.keys()
        self.cmb_data.clear()
        self.cmb_data.addItems(keysList)
        self.appControl.updateDataList(keysList)

    def setFilePath(self):
        """Select a directory and call setFolderPath and replaceLastPath from appControl.
        Args:
            Nothing.
        Return:
            Nothing.
        """
        try:
            filePath = QFileDialog.getOpenFileName(self, "Select File")[0]
            self.le_filePath.setText(filePath)
            self.appControl.showOnConsole("filePath found !", "green")
            self.changeFilePathColorIndicator("green")
        except Exception as e:
            e = str(e)
            self.appControl.showOnConsole(e, "red")

    def resetData(self):
        self.cmb_data.clear()
        self.appControl.clearGraphViewData()
        self.modelData.resetDataDict()
        self.ind_dataName.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.ind_filePath.setStyleSheet("QCheckBox::indicator{background-color: rgb(0,255,0);}")
        self.pb_extract.setEnabled(True)

    def preview(self):
        try:
            key = self.cmb_data.currentText()
            data = self.modelData.getData(key)
            xValues = data.get("xValues")
            yValues = data.get("yValues")
            preview = [" xValues | yValues"]
            for i, item in enumerate(xValues):
                line = str(item) + " | " + str(yValues[i])
                preview.append(line)
            self.lw_preview.clear()
            self.lw_preview.addItems(preview)
        except:
            self.lw_preview.clear()
