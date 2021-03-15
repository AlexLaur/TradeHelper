from PySide2 import QtCore, QtGui, QtWidgets

from libs.events_handler import EventHandler
from ui import welcome_widget, welcome_ticker_widget


class WelcomeWidget(QtWidgets.QWidget, welcome_widget.Ui_WelcomeWidget):
    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__(parent)

        self.setupUi(self)

        self.signal = EventHandler()
        self.grid = QtWidgets.QGridLayout(self.wgt_welcome_content)

    def build_welcome_page(self, data):
        col = 0
        max_col = 2
        row = 0
        for item in data:
            btn = ButtonRapidAccess(item=item)
            btn.clicked.connect(self._on_ticker_choosen)
            self.grid.addWidget(btn, row, col)

            if col == max_col:
                col = 0
                row += 1
            else:
                col += 1

    @QtCore.Slot()
    def _on_ticker_choosen(self):
        """Called when a ticker is choosen (click on it (button))"""
        sender = self.sender()
        ticker_name = sender.ticker
        self.signal.sig_ticker_choosen.emit(ticker_name)

    @QtCore.Slot(list)
    def _on_favorite_loaded(self, data):
        """Called when favorite have been loaded and are ready to be displayed

        :param data: The favorite data
        :type data: list
        """
        self.build_welcome_page(data=data)


class ButtonRapidAccess(
    QtWidgets.QPushButton, welcome_ticker_widget.Ui_WelcomeTickerWidget
):
    def __init__(self, item, parent=None):
        super(ButtonRapidAccess, self).__init__(parent)

        self.setupUi(self)
        self.setFlat(True)

        self.setFixedHeight(150)
        self.setFixedWidth(150)

        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.ticker = item.get("ticker", None)
        self.name = item.get("name", None)

        self.lab_ticker_name.setText(
            "{name} - {ticker}".format(name=self.name, ticker=self.ticker)
        )

        self.resize_thumbnail()

    def resize_thumbnail(self):
        pixmap = self.lab_ticker_img.pixmap()
        pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.lab_ticker_img.setPixmap(pixmap)
