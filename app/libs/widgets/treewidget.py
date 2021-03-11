from PySide2 import QtCore, QtGui, QtWidgets


class TreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent=parent)

    def get_all_items(self, item: object) -> list:
        """Get all items of the treewidget

        :param item: The first item (should be the invisibleRootItem)
        :type item: QTreeWidgetItem
        :return: The list of all items
        :rtype: list
        """
        result = [item]
        for index in range(item.childCount()):
            child = item.child(index)
            result.extend(self.get_all_items(child))
        return result

    def search_items(self, text: str, column: int = 0):
        """Search all items correcponding to the text

        :param text: The text to search
        :type text: str
        :param column: The column on which to search, defaults to 0
        :type column: int, optional
        """
        found = self.findItems(text, QtCore.Qt.MatchContains, column)
        all_items = self.get_all_items(self.invisibleRootItem())
        # Hide all items
        for item in all_items:
            item.setHidden(True)
        # Unhide founded items
        for item in found:
            item.setHidden(False)
        # Unhides all items if no text
        if not text:
            for item in all_items:
                item.setHidden(False)


class TickersTreeWidget(TreeWidget):
    def __init__(self, parent=None):
        super(TickersTreeWidget, self).__init__(parent=parent)
