import os
import json

from PySide2 import QtCore, QtGui, QtWidgets
import yfinance as yf

import resources_rc

from resources.style import style
from libs.events_handler import EventHandler
from libs.tickers_dialog import TickersDialogWindow
from libs.widgets.busywidget import BusyIndicator
from libs.thread_pool import ThreadPool
from libs.graph.candlestick import CandlestickItem

from ui import main_window

from utils import utils
from utils import decorators

SCRIPT_PATH = os.path.dirname(__file__)


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None, data=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)

        # Constants
        self.tickers_dialog = None
        self.tool_bar.init_toolbar()

        # Load all components
        self.tickers_dialog = TickersDialogWindow(parent=self, tickers=data)
        self.busy_indicator = BusyIndicator(parent=self)
        self.thread_pool = ThreadPool()
        self.signals = EventHandler()

        # Signals
        self.lie_ticker.mousePressEvent = self.tickers_dialog.show
        self.tickers_dialog.signal.sig_ticker_choosen.connect(
            self._on_ticker_selected
        )
        self.signals.sig_ticker_infos_fetched.connect(
            self._on_process_ticker_data
        )
        self.thread_pool.signals.sig_thread_pre.connect(
            self.busy_indicator.show
        )
        self.thread_pool.signals.sig_thread_post.connect(
            self.busy_indicator.hide
        )
        self.wgt_indicators.signals.sig_indicator_switched.connect(
            self._on_indicator_switched
        )
        self.action_reload_indicators.triggered.connect(
            self.wgt_indicators.reload_indicators
        )
        self.tool_bar.signals.sig_action_triggered.connect(
            self._on_action_triggered
        )

    def _retrieve_data(self):
        """Retrieve data from the API"""
        ticker = yf.Ticker(self.lie_ticker.text())
        data = ticker.history(period="1y", interval="1d", start="2018-01-01")
        self.signals.sig_ticker_infos_fetched.emit(data)

    @QtCore.Slot(object)
    def _on_process_ticker_data(self, data):
        """Called when informations about the ticker are available.

        :param data: The data of the ticker
        :type data: panda dataframe
        """
        self.wgt_graph.graph.plot_quotation(data)
        if self.stw_main.currentIndex() == 0:
            self.stw_main.slide_in_next()

    @QtCore.Slot(str)
    def _on_ticker_selected(self, ticker_name: str):
        """Callback on ticker selected from the ticker dialog

        :param ticker_name: The name of the selected ticker
        :type ticker_name: str
        """
        self.lie_ticker.setText(ticker_name)
        self.thread_pool.execution(function=self._retrieve_data)

    @QtCore.Slot(object, bool)
    def _on_indicator_switched(self, indicator: object, state: bool):
        """Callback on indicator activated from the indicator widget

        :param indicator: The selected indicator
        :type indicator: dict
        """
        if state:
            indicator.create_indicator(graph_view=self.wgt_graph.graph)
        else:
            indicator.remove_indicator(graph_view=self.wgt_graph.graph)

    @QtCore.Slot(str)
    def _on_action_triggered(self, action: str):
        """Callback on action triggered from the toolbar

        :param action: The action to find and call
        :type action: str
        """
        action_obj = utils.find_method(module=action, obj=self)
        if action_obj:
            action_obj()

    def resizeEvent(self, event):
        if self.tickers_dialog:
            self.tickers_dialog.move_to()

    def moveEvent(self, event):
        if self.tickers_dialog:
            ...
