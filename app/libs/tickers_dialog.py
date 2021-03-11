from PySide2 import QtGui, QtCore, QtWidgets

from libs.events_handler import EventHandler
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
        self.trw_all_tickers.itemClicked.connect(self.choose_ticker)
        self.lie_ticker_search.textChanged.connect(
            self.trw_all_tickers.search_items
        )
        self.pub_close.clicked.connect(self.close)
        self.trw_all_tickers.customContextMenuRequested.connect(self._set_menu)

    def build_ticker_tree(self, data: list):
        """Build the data inside the treewidget

        :param data: All tickers
        :type data: list
        """
        for ticker, company in data.items():
            item = QtWidgets.QTreeWidgetItem(
                self.trw_all_tickers, [ticker, company]
            )

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

    def move_to(self, pos=None):
        if not pos:
            self.move(self.parent().rect().center() - self.rect().center())
        else:
            self.move(pos)

    def show(self, *args, **kwargs):
        self.lie_ticker_search.clear()
        self.lie_ticker_search.setFocus()
        super(TickersDialogWindow, self).show()

    def _set_menu(self, event):
        print("menu")
        menu = QtWidgets.QMenu(self)

        menu.addAction("Set a quick access")

        point = QtCore.QPoint(QtGui.QCursor.pos())

        menu.exec_(event.pos())
