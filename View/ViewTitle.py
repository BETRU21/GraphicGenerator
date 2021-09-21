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
        self.pb_plot.clicked.connect(self.plotSubtitles)
        self.pb_legend.clicked.connect(self.addSpecificLegend)
        self.pb_deleteLegend.clicked.connect(self.deleteSpecificLegend)
        self.pb_legends.clicked.connect(self.addLegends)
        self.pb_deleteLegends.clicked.connect(self.deleteLegends)

    def setupWidgets(self):
        self.cmb_pos.clear()
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def addSpecificLegend(self):
        pass

    def deleteSpecificLegend(self):
        pass

    def addLegends(self):
        pass

    def deleteLegends(self):
        pass


    def plotTitle(self):
        title = self.le_title.text()
        self.modelGraphic.addMainTitle(title)

    def plotSubtitles(self):
        positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
        position = (int(positionStr[0]), int(positionStr[1]))
        subtitle = self.le_subtitle.text()
        subtitleX = self.le_xAxis.text()
        subtitleY = self.le_yAxis.text()
        self.modelGraphic.addSubtitle(position, subtitle)
        self.modelGraphic.addXSubtitle(position, subtitleX)
        self.modelGraphic.addYSubtitle(position, subtitleY)

    def enableWidgets(self):
        self.le_title.setEnabled(True)
        self.le_subtitle.setEnabled(True)
        self.le_xAxis.setEnabled(True)
        self.le_yAxis.setEnabled(True)
        self.pb_plot.setEnabled(True)
        self.cmb_pos.setEnabled(True)


