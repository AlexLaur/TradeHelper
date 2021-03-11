from PySide2 import QtCore, QtGui, QtWidgets


class TableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(TableWidgetItem, self).__init__(parent)

        self.__dict__.update(kwargs)

        if text:
            self.setText(text)
