from PySide2 import QtCore, QtGui, QtWidgets
from libs.widgets.treewidgetitem import TreeWidgetItem


class TreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent=parent)

    def get_all_items(
        self, item: object, include_invisible: bool = True
    ) -> list:
        """Get all items of the treewidget

        :param item: The first item (should be the invisibleRootItem)
        :type item: QTreeWidgetItem
        :param include_invisible: Include the invisibleRootItem in the result
        :type include_invisible: bool
        :return: The list of all items
        :rtype: list
        """
        result = []
        if include_invisible:
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

    def set_header(self):
        """Sets a custom header to the treewidget"""
        header = QtWidgets.QHeaderView(QtCore.Qt.Horizontal, self)
        self.setHeader(header)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.resizeSection(0, 150)
        header.setSectionsClickable(True)


class FavoritesTreeWidget(TreeWidget):
    def __init__(self, parent=None):
        super(FavoritesTreeWidget, self).__init__(parent=parent)

    def remove_favorite(self, ticker: dict):
        """Remove a favorite from the treewidget

        :param ticker: The ticker which has been deleted
        :type ticker: dict
        """
        _all = self.get_all_items(
            item=self.invisibleRootItem(), include_invisible=False
        )
        for item in _all:
            if item.favorite.get("ticker") != ticker.get(
                "ticker"
            ) or item.favorite.get("name") != ticker.get("name"):
                continue
            index = self.indexOfTopLevelItem(item)
            self.takeTopLevelItem(index)
            break

    def add_favorite(self, ticker: dict):
        """Add a favorite to the list

        :param ticker: The ticker which has been added
        :type ticker: dict
        """
        self._add_favorite(ticker=ticker)

    def _add_favorite(self, ticker: dict):
        """Private method to add an item inside the treewidget

        :param ticker: The ticker to add
        :type ticker: dict
        """
        text = "{name} - {ticker}".format(
            name=ticker.get("name"), ticker=ticker.get("ticker")
        )
        item = TreeWidgetItem(
            parent=self,
            text=[text],
            favorite=ticker,
            icon=QtGui.QIcon(":/svg/candle-sticks.svg"),
        )
