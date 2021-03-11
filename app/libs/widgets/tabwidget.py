from PySide2 import QtCore, QtGui, QtWidgets


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent=parent)
