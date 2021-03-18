from PySide2 import QtCore, QtGui, QtWidgets

from libs.events_handler import EventHandler
from libs.widgets.treewidgetitem import TreeWidgetItem
from ui.favorites_widget import Ui_FavoritesWidget


class FavoritesWidget(QtWidgets.QWidget, Ui_FavoritesWidget):
    def __init__(self, parent=None):
        super(FavoritesWidget, self).__init__(parent)

        self.setupUi(self)

        # Constans
        self.signals = EventHandler()

        # Signals
        self.trw_favorites.itemClicked.connect(self._on_favorite_clicked)

    def build_favorites(self, favorites):
        """Build the treewidgets of favorites

        :param favorites: All favorites
        :type favorites: list
        """
        for favorite in favorites:
            text = "{name} - {ticker}".format(
                name=favorite.get("name"), ticker=favorite.get("ticker")
            )
            item = TreeWidgetItem(
                parent=self.trw_favorites,
                text=[text],
                favorite=favorite,
                icon=QtGui.QIcon(":/svg/candle-sticks.svg"),
            )

    @QtCore.Slot()
    def _on_favorite_clicked(self, item):
        """Called when a favorite is clicked"""
        ticker_name = item.favorite.get("ticker")
        self.signals.sig_favorite_clicked.emit(ticker_name)

    @QtCore.Slot(list)
    def _on_favorite_loaded(self, data):
        """Called when favorite have been loaded and are ready to be displayed

        :param data: The favorite data
        :type data: list
        """
        self.build_favorites(favorites=data)
