from View.ViewData import ViewData
from View.ViewGraph import ViewGraph
from View.ViewConsole import ViewConsole
from View.ViewCurvefit import ViewCurvefit
from View.ViewTitle import ViewTitle
from Model.Graphic import Graphic
from Model.Curvefit import Curvefit
from Model.DataExtractor import DataExtractor
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from PyQt5 import uic
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '/ui{}MainWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.modelGraphic = Graphic()
        self.modelData = DataExtractor()
        self.modelCurvefit = Curvefit()
        self.createsComponentsAndPointers()
        self.setupWindowTabs()

    def setupWindowTabs(self): #01
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.addTab(self.dataView, "Extract Data")
        self.tabWidget.addTab(self.graphView, "Graph")
        self.tabWidget.addTab(self.curvefitView, "Curvefit")
        self.tabWidget.addTab(self.titleView, "Title")
        self.tabWidget.addTab(self.consoleView, "Console")

    def createsComponentsAndPointers(self): #02
        # Components
        self.graphView = ViewGraph(self.modelGraphic, self.modelData)
        self.consoleView = ViewConsole()
        self.dataView = ViewData(self.modelData)
        self.curvefitView = ViewCurvefit(self.modelGraphic, self.modelData, self.modelCurvefit)
        self.titleView = ViewTitle(self.modelGraphic, self.modelData)
        # Pointers
        self.curvefitView.consoleView = self.consoleView

        self.titleView.consoleView = self.consoleView

        self.graphView.consoleView = self.consoleView
        self.graphView.curvefitView = self.curvefitView
        self.graphView.titleView = self.titleView

        self.dataView.consoleView = self.consoleView
        self.dataView.graphView = self.graphView
        self.dataView.curvefitView = self.curvefitView
