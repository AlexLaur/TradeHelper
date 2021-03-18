import webbrowser
from PySide2 import QtWidgets, QtGui

class LabelTitle(QtWidgets.QLabel):
    def __init__(self, link=None, size=20):
        super(LabelTitle, self).__init__()
        self.link = link
        self.setFont(QtGui.QFont("Times", size))

    def mousePressEvent(self, event) -> None:
        webbrowser.open(self.link)
