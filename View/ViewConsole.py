from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5 import QtGui
import os

MainWindowPath = os.path.dirname(os.path.realpath(__file__)) + '{}ConsoleWindow.ui'.format(os.sep)
Ui_MainWindow, QtBaseClass = uic.loadUiType(MainWindowPath)

class ViewConsole(QWidget, Ui_MainWindow):
    def __init__(self):
        super(ViewConsole, self).__init__()
        self.setupUi(self)
        self.appControl = None
        self.te_Console.clear()

    def showOnConsole(self, text, color=None):
        """Show text on the console view.
        Args:
            text(str): The text to show on console.
            color(str): (facultative), "red","green" or nothing
        return:
            Nothing. 
        """
        if color == None:
            HEX = "#ffffff"
        else:
            if color == "red":
                HEX = "#ff0000"
            elif color == "green":
                HEX = "#0dff00"
            else:
                HEX = "#ffffff"
        self.te_Console.setTextColor(QtGui.QColor(HEX))
        self.te_Console.append(text)