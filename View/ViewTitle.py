from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import sys
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}TitleWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

# TODO : Faire les fonctionnalités de légendes et titres.

class ViewTitle(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData):
        super(ViewTitle, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.setupWidgets()
        self.connectWidgets()

    def connectWidgets(self):
        self.le_title.textChanged.connect(self.plotTitle)
        self.le_xAxis.textChanged.connect(self.plotXSubtitle)
        self.le_yAxis.textChanged.connect(self.plotYSubtitle)
        self.le_subtitle.textChanged.connect(self.plotSubtitle)
        self.pb_legend.clicked.connect(self.addLegendWithPosition)
        self.pb_deleteLegend.clicked.connect(self.deleteLegendWithPosition)
        self.pb_legends.clicked.connect(self.addLegends)
        self.pb_deleteLegends.clicked.connect(self.deleteLegends)
        self.cmb_pos.currentIndexChanged.connect(self.resetText)

    def setupWidgets(self):
        self.cmb_pos.clear()
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def addLegendWithPosition(self):
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            self.modelGraphic.addLegend(position)
        except Exception as e:
            e = str(e)
            self.consoleView.showOnConsole(e, "red")

    def deleteLegendWithPosition(self):
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            self.modelGraphic.deleteLegend(position)
        except Exception as e:
            e = str(e)
            self.consoleView.showOnConsole(e, "red")

    def addLegends(self):
        try:
            self.modelGraphic.addLegends()
        except Exception as e:
            e = str(e)
            self.consoleView.showOnConsole(e, "red")

    def deleteLegends(self):
        try:
            self.modelGraphic.deleteLegends()
        except Exception as e:
            e = str(e)
            self.consoleView.showOnConsole(e, "red")

    def resetText(self):
        self.le_subtitle.clear()
        self.le_xAxis.clear()
        self.le_yAxis.clear()

    def plotTitle(self):
        title = self.le_title.text()
        self.modelGraphic.addMainTitle(title)

    def plotSubtitle(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        subtitle = self.le_subtitle.text()
        self.modelGraphic.addSubtitle(position, subtitle)

    def plotXSubtitle(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        subtitleX = self.le_xAxis.text()
        self.modelGraphic.addXSubtitle(position, subtitleX)

    def plotYSubtitle(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        subtitleY = self.le_yAxis.text()
        self.modelGraphic.addYSubtitle(position, subtitleY)

    def enableWidgets(self):
        self.le_title.setEnabled(True)
        self.le_subtitle.setEnabled(True)
        self.le_xAxis.setEnabled(True)
        self.le_yAxis.setEnabled(True)
        self.cmb_pos.setEnabled(True)


