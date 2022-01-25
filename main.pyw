from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from View.mainWindow import MainWindow as Window
import ctypes
import sys
import os

appID = "GraphGenerator"
if os.name == 'nt':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
elif os.name == 'posix':
    pass

applicationPath = os.path.abspath("")

"""
|| Error code chart ||
    ViewData: VD#XX
    ViewGraph: VG#XX
    ViewTitle: VT#XX
    MainWindow: MW#XX
    ViewCurvefit: VC#XX
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QMainWindow()
    win = Window()
    win.setWindowIcon(QIcon(applicationPath + "{0}View{0}logo{0}logo.ico".format(os.sep)))
    win.setWindowTitle("GraphGenerator")
    win.show()
    sys.exit(app.exec())
