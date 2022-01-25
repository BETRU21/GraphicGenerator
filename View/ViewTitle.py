from PyQt5.QtWidgets import QColorDialog, QWidget
from PyQt5 import uic
import sys
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}TitleWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewTitle(QWidget, Ui_MainWindow):
    def __init__(self, modelGraphic, modelData):
        super(ViewTitle, self).__init__()
        self.setupUi(self)
        self.modelGraphic = modelGraphic
        self.modelData = modelData
        self.setupWidgets()
        self.connectWidgets()

    def connectWidgets(self): #01
        self.le_title.textChanged.connect(self.plotTitle)
        self.le_xAxis.textChanged.connect(self.plotXSubtitle)
        self.le_yAxis.textChanged.connect(self.plotYSubtitle)
        self.le_subtitle.textChanged.connect(self.plotSubtitle)
        self.pb_legend.clicked.connect(self.addLegendWithPosition)
        self.pb_deleteLegend.clicked.connect(self.deleteLegendWithPosition)
        self.pb_legends.clicked.connect(self.addLegends)
        self.pb_deleteLegends.clicked.connect(self.deleteLegends)
        self.cmb_pos.currentIndexChanged.connect(self.resetText)
        self.sb_title.valueChanged.connect(self.plotTitle)
        self.sb_subtitle.valueChanged.connect(self.plotSubtitle)
        self.sb_xAxisTitle.valueChanged.connect(self.plotXSubtitle)
        self.sb_yAxisTitle.valueChanged.connect(self.plotYSubtitle)

    def setupWidgets(self): #02
        self.cmb_pos.clear()
        for i, position in enumerate(self.modelGraphic.positions):
            position = str(position)
            self.cmb_pos.addItem(position)

    def addLegendWithPosition(self): #03
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            font = self.sb_legend.value()
            self.modelGraphic.addLegend(position, fontSize=font)
        except Exception as e:
            e = str(e) + " |ERROR:VT#03|"
            self.consoleView.showOnConsole(e, "red")

    def deleteLegendWithPosition(self): #04
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            self.modelGraphic.deleteLegend(position)
        except Exception as e:
            e = str(e) + " |ERROR:VT#04|"
            self.consoleView.showOnConsole(e, "red")

    def addLegends(self): #05
        try:
            font = self.sb_legend.value()
            self.modelGraphic.addLegends(fontSize=font)
        except Exception as e:
            e = str(e) + " |ERROR:VT#05|"
            self.consoleView.showOnConsole(e, "red")

    def deleteLegends(self): #06
        try:
            self.modelGraphic.deleteLegends()
        except Exception as e:
            e = str(e) + " |ERROR:VT#06|"
            self.consoleView.showOnConsole(e, "red")

    def resetText(self): #07
        self.le_subtitle.clear()
        self.le_xAxis.clear()
        self.le_yAxis.clear()

    def plotTitle(self): #08
        try:
            title = self.le_title.text()
            font = self.sb_title.value()
            self.modelGraphic.addMainTitle(title, fontSize=font)
        except:
            pass

    def plotSubtitle(self): #09
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            subtitle = self.le_subtitle.text()
            font = self.sb_subtitle.value()
            self.modelGraphic.addSubtitle(position, subtitle, fontSize=font)
        except:
            pass

    def plotXSubtitle(self): #10
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            subtitleX = self.le_xAxis.text()
            font = self.sb_xAxisTitle.value()
            self.modelGraphic.addXSubtitle(position, subtitleX, fontSize=font)
        except:
            pass

    def plotYSubtitle(self): #11
        try:
            positionStr = self.cmb_pos.currentText()[1:-1].split(", ")
            position = (int(positionStr[0]), int(positionStr[1]))
            subtitleY = self.le_yAxis.text()
            font = self.sb_yAxisTitle.value()
            self.modelGraphic.addYSubtitle(position, subtitleY, fontSize=font)
        except:
            pass

    def enableWidgets(self): #12
        self.le_title.setEnabled(True)
        self.le_subtitle.setEnabled(True)
        self.le_xAxis.setEnabled(True)
        self.le_yAxis.setEnabled(True)
        self.cmb_pos.setEnabled(True)
        self.pb_legend.setEnabled(True)
        self.pb_legends.setEnabled(True)
        self.pb_deleteLegend.setEnabled(True)
        self.pb_deleteLegends.setEnabled(True)
        self.sb_title.setEnabled(True)
        self.sb_subtitle.setEnabled(True)
        self.sb_xAxisTitle.setEnabled(True)
        self.sb_yAxisTitle.setEnabled(True)
        self.sb_legend.setEnabled(True)
