from PySide2 import QtCore, QtGui, QtWidgets


class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(TreeWidgetItem, self).__init__(parent, text)

        self.__dict__.update(kwargs)

        checkable = kwargs.get("checkable", False)
        if checkable:
            self.setCheckState(0, QtCore.Qt.Unchecked)
