import webbrowser
from PySide2 import QtWidgets, QtGui

class LabelTitle(QtWidgets.QLabel):
    def __init__(self, link=None, size=20):
        super(LabelTitle, self).__init__()

        self.font = "Times"
        self.set_font_size(size)

    def set_font_size(self, size):
        self.setFont(QtGui.QFont(self.font, size))

    def set_link(self, link):
        self.link = link

    def mousePressEvent(self, event) -> None:
        webbrowser.open(self.link)
