from PySide2 import QtGui, QtCore, QtWidgets

from libs.events_handler import EventHandler
from libs.widgets.treewidgetitem import TreeWidgetItem
from ui import tickers_dialog


class TickersDialogWindow(
    QtWidgets.QDialog, tickers_dialog.Ui_TickersDialogWindow
):
    def __init__(self, parent=None, tickers=[]):
        super(TickersDialogWindow, self).__init__(parent=parent)

        self.setWindowFlags(
            QtCore.Qt.Window
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setupUi(self)

        # Set the header of the treewidget
        self.trw_all_tickers.set_header()

        # Constants
        self.tickers = tickers
        self.signal = EventHandler()

        # Build widgets data
        self.build_ticker_tree(data=self.tickers)

        # Signals
        self.trw_all_tickers.itemDoubleClicked.connect(self.choose_ticker)
        self.trw_all_tickers.itemChanged.connect(self.favorite_item)

        self.lie_ticker_search.textChanged.connect(
            self.trw_all_tickers.search_items
        )
        self.pub_close.clicked.connect(self.close)

    def build_ticker_tree(self, data: list):
        """Build the data inside the treewidget

        :param data: All tickers
        :type data: list
        """

        for ticker, infos in data.items():
            company = infos[0]
            market = infos[1]
            item = TreeWidgetItem(
                self.trw_all_tickers,
                [ticker, company, market],
                checkable=True,
                ticker=ticker,
                name=company,
                market=market,
            )

    def update_ticker_favorite_state(self, favorite):
        """Update the state of the favorite checkbox

        :param favorite: The list of favorite
        :type favorite: list
        """
        self.signal.blockSignals(True)
        for item in self.trw_all_tickers.get_all_items(
            item=self.trw_all_tickers.invisibleRootItem(),
            include_invisible=False,
        ):
            if {"ticker": item.ticker, "name": item.name} in favorite:
                item.setCheckState(0, QtCore.Qt.Checked)
            else:
                item.setCheckState(0, QtCore.Qt.Unchecked)
        self.signal.blockSignals(False)

    def choose_ticker(self, item: QtWidgets.QTreeWidgetItem, column: int):
        """Click on an item inside the treewidget

        :param item: The selected item
        :type item: QTreeWidgetItem
        :param column: The column selected
        :type column: int
        """
        ticker_name = item.text(0)
        self.signal.sig_ticker_choosen.emit(ticker_name)
        self.close()

    def favorite_item(self, item: QtWidgets.QTreeWidgetItem, column: int):
        """Promote or demote an item as favorite

        :param item: The item
        :type item: QtWidgets.QTreeWidgetItem
        :param column: The column clicked
        :type column: int
        """
        ticker = {"ticker": item.ticker, "name": item.name}
        if item.is_checked():
            self.signal.sig_ticker_added_favorite.emit(ticker)
        else:
            self.signal.sig_ticker_removed_favorite.emit(ticker)

    def move_to(self, pos=None):
        if not pos:
            self.move(self.parent().rect().center() - self.rect().center())
        else:
            self.move(pos)

    def show(self, *args, **kwargs):
        self.lie_ticker_search.clear()
        self.lie_ticker_search.setFocus()
        super(TickersDialogWindow, self).show()

    @QtCore.Slot(list)
    def _on_favorite_loaded(self, favorite):
        """Called when the favorite tickers are loaded

        :param favorite: List of favorite
        :type favorite: list
        """
        self.update_ticker_favorite_state(favorite=favorite)
