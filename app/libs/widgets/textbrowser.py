from PySide2 import QtWidgets, QtGui

class Description(QtWidgets.QTextBrowser):
    def __init__(self, text):
        super(Description, self).__init__()
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        if text:
            self.setText("text")
            self.setFont(QtGui.QFont("Times", 10))
