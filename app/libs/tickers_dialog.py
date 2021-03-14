from PySide2 import QtGui, QtCore, QtWidgets

from libs.events_handler import EventHandler
from libs.widgets.pushbutton import FavoriteButton
from libs.widgets.treewidgetitem import TreeWidgetItem
from ui import tickers_dialog


class TickersDialogWindow(
    QtWidgets.QDialog, tickers_dialog.Ui_TickersDialogWindow
):
    def __init__(self, parent=None, tickers={}):
        super(TickersDialogWindow, self).__init__(parent=parent)

        self.setWindowFlags(
            QtCore.Qt.Window
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setupUi(self)

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
        for ticker, company in data.items():
            item = TreeWidgetItem(
                self.trw_all_tickers, [ticker, company], checkable=True
            )
            # btn = FavoriteButton()
            # self.trw_all_tickers.setItemWidget(item, 2, btn)

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
        print(item)

    def move_to(self, pos=None):
        if not pos:
            self.move(self.parent().rect().center() - self.rect().center())
        else:
            self.move(pos)

    def show(self, *args, **kwargs):
        self.lie_ticker_search.clear()
        self.lie_ticker_search.setFocus()
        super(TickersDialogWindow, self).show()
