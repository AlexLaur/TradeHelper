import os
import json
from PySide2 import QtCore, QtGui, QtWidgets

from libs.events_handler import EventHandler
from ui import welcome_widget, welcome_ticker_widget

SCRIPT_PATH = os.path.dirname(__file__)


class WelcomeWidget(QtWidgets.QWidget, welcome_widget.Ui_WelcomeWidget):
    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__(parent)

        self.setupUi(self)

        self.signal = EventHandler()
        self.grid = QtWidgets.QGridLayout(self.wgt_welcome_content)

        with open(
            os.path.join(os.path.dirname(SCRIPT_PATH), "data", "welcome.json"),
            "r",
        ) as f:
            data = json.load(f)

        self.build_welcome_page(data)
        # self.scr_area.setWidgetResizable(False)

    def build_welcome_page(self, data):
        col = 0
        max_col = 2
        row = 0
        for item in data:
            btn = ButtonRapidAccess(item=item)
            btn.clicked.connect(self.choose_ticker)
            self.grid.addWidget(btn, row, col)

            if col == max_col:
                col = 0
                row += 1
            else:
                col += 1

    def choose_ticker(self):
        """Click on a button which represent a ticker"""
        sender = self.sender()
        ticker_name = sender.ticker
        self.signal.sig_ticker_choosen.emit(ticker_name)


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
