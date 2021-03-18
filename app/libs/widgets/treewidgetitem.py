from PySide2 import QtCore, QtGui, QtWidgets


class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(TreeWidgetItem, self).__init__(parent, text)

        self.__dict__.update(kwargs)

        checkable = kwargs.get("checkable", False)
        if checkable:
            self.setCheckState(0, QtCore.Qt.Unchecked)

        icon = kwargs.get("icon", None)
        if icon:
            self.setIcon(0, icon)

    def is_checked(self) -> bool:
        """Return True if the item is checked, False instead

        :return: The status of the checkstate
        :rtype: bool
        """
        if self.checkState(0) == QtCore.Qt.Checked:
            return True
        return False
