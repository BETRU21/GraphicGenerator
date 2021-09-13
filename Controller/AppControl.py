import numpy as np
import sys
import os

applicationPath = os.path.abspath("")

class AppControl():
    def __init__(self, modelGraphic):
        self.modelGraphic = modelGraphic
        self.graphView = None
        self.consoleView = None
        self.dataView = None

    def showOnConsole(self, text, color=None):
        """Call showOnConsole from console view.
        Args:
            text(str): The text to show on console.
            [Facultative]
            color(str): (facultative), "red","green" or nothing.
        return:
            None
        """
        self.consoleView.showOnConsole(text, color)

    def updateDataList(self, keysList):
        self.graphView.updateDataList(keysList)

    def clearGraphViewData(self):
        self.graphView.cmb_data.clear()
