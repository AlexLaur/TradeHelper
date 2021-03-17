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

    # def set_header(self):
    #     headerView = QtWidgets.QHeaderView(QtCore.Qt.Horizontal, self)
    #     self.setHeader(headerView)
    #     headerView.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
    #     headerView.setSectionsClickable(True)

    #     # Favorite column
    #     # self.header().resizeSection(2, 20)
    #     # self.header().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


class FavoritesTreeWidget(TreeWidget):
    def __init__(self, parent=None):
        super(FavoritesTreeWidget, self).__init__(parent=parent)

    def remove_favorite(self, ticker: dict):
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
        self._add_favorite(ticker=ticker)

    def _add_favorite(self, ticker):
        text = "{name} - {ticker}".format(
            name=ticker.get("name"), ticker=ticker.get("ticker")
        )
        item = TreeWidgetItem(
            parent=self,
            text=[text],
            favorite=ticker,
            icon=QtGui.QIcon(":/svg/candle-sticks.svg"),
        )
