from PySide2 import QtCore, QtGui, QtWidgets

from libs.events_handler import EventHandler
from ui.favorites_widget import Ui_FavoritesWidget


class FavoritesWidget(QtWidgets.QWidget, Ui_FavoritesWidget):
    def __init__(self, parent=None):
        super(FavoritesWidget, self).__init__(parent)

        self.setupUi(self)

        # Constans
        self.signals = EventHandler()

        # Signals
        self.trw_favorites.itemClicked.connect(self._on_favorite_clicked)
        self.lie_search_favorite.textChanged.connect(
            self.trw_favorites.search_items
        )

    def build_favorites(self, favorites):
        """Build the treewidgets of favorites

        :param favorites: All favorites
        :type favorites: list
        """
        for favorite in favorites:
            self.trw_favorites.add_favorite(ticker=favorite)

    @QtCore.Slot(dict)
    def _on_favorite_added(self, ticker):
        """Called when a ticker is marked as favorite

        :param ticker: The ticker to add as favorite
        :type ticker: dict
        """
        self.trw_favorites.add_favorite(ticker=ticker)

    @QtCore.Slot(dict)
    def _on_favorite_removed(self, ticker):
        """Called when a ticker is removed from favorites

        :param ticker: The ticker to remove from favorites
        :type ticker: dict
        """
        self.trw_favorites.remove_favorite(ticker=ticker)

    @QtCore.Slot(object)
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
