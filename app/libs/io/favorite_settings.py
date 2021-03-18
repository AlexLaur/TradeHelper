import os
import json

from PySide2 import QtCore

from libs.events_handler import EventHandler


class FavoritesManager(QtCore.QObject):
    def __init__(self, parent):
        super(FavoritesManager, self).__init__(parent)

        # Constants
        self.signals = EventHandler()
        self._app_home = os.environ.get("APP_HOME")
        self._favorites_path = os.path.join(
            self._app_home, "favorite", "favorite.json"
        )
        self._favorites = []

    def load_favorite(self) -> list:
        """Load favorite from the file

        :return: The loaded favorite
        :rtype: list
        """
        if not self._check_favorites():
            return self._favorites
        with open(self._favorites_path, "r") as f:
            self._favorites = json.load(f)
        self.signals.sig_favorite_loaded.emit(self._favorites)
        return self._favorites

    def save_favorites(self):
        """Save favorites into the file"""
        if not self._check_favorites():
            self.create_favorite()
        with open(self._favorites_path, "w") as f:
            json.dump(self._favorites, f)
        self.signals.sig_favorite_saved.emit(self._favorites)

    def create_favorite(self) -> bool:
        """Create the favorite file if it doesn't exists

        :return: True if exists, False if the creation failed
        :rtype: bool
        """
        if self._check_favorites():
            return True
        if not os.path.exists(os.path.dirname(self._favorites_path)):
            try:
                os.mkdir(os.path.dirname(self._favorites_path))
            except Exception as error:  # TODO cath correct error
                print(error)
        # create file in all cases
        try:
            open(self._favorites_path, "w").close()
        except Exception as error:
            print(error)
            return False
        self.signals.sig_favorite_created.emit(self._favorites)
        return True

    def _check_favorites(self):
        """Check if the favorite file exists

        :return: True or False
        :rtype: bool
        """
        if os.path.exists(self._favorites_path):
            return True
        return False

    def add_ticker_favorite(self, ticker_data: dict):
        """Add a new ticker to the favorite

        :param ticker_data: The ticker to add
        :type ticker_data: dict
        """
        self._favorites.append(ticker_data)
        self.signals.sig_favorite_added.emit(ticker_data)

    def remove_ticker_favorite(self, ticker_data: dict):
        """Remove a ticker from the favorite

        :param ticker_data: The ticker to remove
        :type ticker_data: dict
        """
        if ticker_data in self._favorites:
            self._favorites.remove(ticker_data)
            self.signals.sig_favorite_removed.emit(ticker_data)

    @QtCore.Slot(dict)
    def _on_add_ticker_favorite(self, ticker_data):
        """Called when a ticker is added to favorite

        :param ticker_data: The added ticker
        :type ticker_data: dict
        """
        self.add_ticker_favorite(ticker_data=ticker_data)

    @QtCore.Slot(dict)
    def _on_remove_ticker_favorite(self, ticker_data: dict):
        """Called when a ticker is removed from favorite

        :param ticker_data: The removed ticker
        :type ticker_data: dict
        """
        self.remove_ticker_favorite(ticker_data=ticker_data)
