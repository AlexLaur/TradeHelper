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
from libs.io.favorite_settings import FavoritesManager
from libs.widgets.sentimentals_widget import Sentimental_Widget_Item
from libs.splashcreen import SplashScreen
from libs.roi_manager import ROIManager

from ui import main_window

from utils import utils
from utils import decorators

SCRIPT_PATH = os.path.dirname(__file__)
TITLE = "TRADING VISUALISATION"

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None, data=None):
        super(MainWindow, self).__init__(parent=parent)

        img = "resources\img\splashscreen.jpg"
        path = os.path.join(SCRIPT_PATH, img)

        self.splash = SplashScreen(path, TITLE)
        # self.splash.show()
        self.splash.show_message("Loading UI...\n\n")
        QtWidgets.QApplication.processEvents()

        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        # Constants
        self.tickers_dialog = None
        self.tool_bar.init_toolbar()

        # Load all components
        self._init_app_home()
        self.tickers_dialog = TickersDialogWindow(parent=self, tickers=data)
        self.busy_indicator = BusyIndicator(parent=self)
        self.thread_pool = ThreadPool()
        self.signals = EventHandler()
        self.favorites_manager = FavoritesManager(parent=self)

        # Signals
        self.lie_ticker.mousePressEvent = self.tickers_dialog.show
        self.tickers_dialog.signal.sig_ticker_choosen.connect(
            self._on_ticker_selected
        )
        self.tickers_dialog.signal.sig_ticker_added_favorite.connect(
            self.favorites_manager._on_add_ticker_favorite
        )
        self.tickers_dialog.signal.sig_ticker_removed_favorite.connect(
            self.favorites_manager._on_remove_ticker_favorite
        )
        self.tickers_dialog.signal.sig_ticker_added_favorite.connect(
            self.wgt_favorites._on_favorite_added
        )
        self.tickers_dialog.signal.sig_ticker_removed_favorite.connect(
            self.wgt_favorites._on_favorite_removed
        )
        self.wgt_favorites.signals.sig_favorite_clicked.connect(
            self._on_ticker_selected
        )
        self.signals.sig_ticker_data_fetched.connect(
            self._on_process_ticker_data
        )
        self.signals.sig_ticker_infos_fetched.connect(
            self.wgt_company._on_ticker_infos
        )
        self.tickers_dialog.signal.sig_ticker_choosen.connect(
            self.wgt_articles._on_get_articles
        )
        self.wgt_favorites.signals.sig_favorite_clicked.connect(
            self.wgt_articles._on_get_articles
        )
        self.tickers_dialog.signal.sig_ticker_choosen.connect(
            self.wid_table_financ.on_set_financials_table
        )
        self.tickers_dialog.signal.sig_ticker_choosen.connect(
            self.set_sentiment_compagny
        )
        self.wgt_favorites.signals.sig_favorite_clicked.connect(
            self.wid_table_financ.on_set_financials_table
        )
        self.wgt_favorites.signals.sig_favorite_clicked.connect(
            self.set_sentiment_compagny
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
        self.favorites_manager.signals.sig_favorite_loaded.connect(
            self.wgt_favorites._on_favorite_loaded
        )
        self.favorites_manager.signals.sig_favorite_loaded.connect(
            self.tickers_dialog._on_favorite_loaded
        )

        self.pub_go_welcome.clicked.connect(self.stw_main.slide_in_prev)
        self.pub_go_graph.clicked.connect(self.stw_main.slide_in_next)
        self.pub_go_market_prev.clicked.connect(self.wgt_markets_2.slide_in_prev)
        self.pub_go_market_next.clicked.connect(self.wgt_markets_2.slide_in_next)

        # Action which needs to be loaded after all signals
        self.splash.show_message("Loading Favorites...\n\n")
        self.favorites_manager.load_favorite()

        self.splash.hide()

    def _init_app_home(self):
        """Init the APP_HOME of the application"""
        base_path = os.path.expanduser("~")
        app_home = os.path.join(base_path, ".trade_helper")
        if not os.path.exists(app_home):
            try:
                os.makedirs(app_home)
            except Exception as error:
                print(error)
        os.environ["APP_HOME"] = app_home

    def _retrieve_data(self):
        """Retrieve data from the API"""
        ticker = yf.Ticker(self.lie_ticker.text())
        self.signals.sig_ticker_infos_fetched.emit(ticker.info)
        data = ticker.history(period="1y", interval="1d", start="2018-01-01")
        self.signals.sig_ticker_data_fetched.emit(data)

    @QtCore.Slot(object)
    def _on_process_ticker_data(self, data):
        """Called when informations about the ticker are available.

        :param data: The data of the ticker
        :type data: panda dataframe
        """
        self.wgt_graph.graph.plot_quotation(data)
        for indicator in self.wgt_indicators.indicators:
            if not indicator.enabled:
                continue
            # Remove indicator
            indicator.remove_indicator(graph_view=self.wgt_graph.graph)
            # Re create indicator
            indicator.create_indicator(graph_view=self.wgt_graph.graph)
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

    @QtCore.Slot(str, dict)
    def _on_action_triggered(self, action: str, args: dict):
        """Callback on action triggered from the toolbar

        :param action: The action to find and call
        :type action: str
        :param args: Args for the action
        :type args: dict
        """
        action_obj = utils.find_method(module=action, obj=self)
        if action_obj:
            action_obj(**args)

    @QtCore.Slot(str)
    def set_sentiment_compagny(self, ticker):
        """This method set the sentimental widget for
        the select tick.
        """
        utils.clear_layout(self.financials_layout)
        widget = Sentimental_Widget_Item()
        widget.set_sentimental_ui(ticker=ticker)
        self.financials_layout.addWidget(widget)

    def resizeEvent(self, event):
        if self.tickers_dialog:
            self.tickers_dialog.move_to()

    def moveEvent(self, event):
        if self.tickers_dialog:
            ...

    def closeEvent(self, event):
        self.favorites_manager.save_favorites()
