from View.ViewData import ViewData
from View.ViewGraph import ViewGraph
from View.ViewConsole import ViewConsole
from Model.Graphic import Graphic
from Model.DataExtractor import DataExtractor
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from PyQt5 import uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}MainWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.modelGraphic = Graphic()
        self.modelData = DataExtractor()
        self.createsComponentsAndPointers()
        self.setupWindowTabs()

    def setupWindowTabs(self):
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.addTab(self.dataView, "Data")
        self.tabWidget.addTab(self.graphView, "Graph")
        self.tabWidget.addTab(self.consoleView, "Console")

    def createsComponentsAndPointers(self):
        # Components
        self.graphView = ViewGraph(self.modelGraphic, self.modelData)
        self.consoleView = ViewConsole()
        self.dataView = ViewData(self.modelData)
        # New Pointers
        self.graphView.consoleView = self.consoleView
        self.dataView.consoleView = self.consoleView
        self.dataView.graphView = self.graphView
