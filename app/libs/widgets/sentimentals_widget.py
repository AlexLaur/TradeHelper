from utils import utils
from ui.sentimentals import Ui_Sentiment_Form
from PySide2 import QtCore, QtGui, QtWidgets
from libs.tradingview_ta import TA_Handler, Interval, Exchange

TICKERS = ['TSLA', 'AAPL', 'MSFT', 'GLE.PA', 'FP.PA']

LVLS = {
    "STRONG_SELL": 10,
    "SELL": 25,
    "NEUTRAL": 50,
    "BUY": 75,
    "STRONG_BUY": 90,
}


class Sentimental_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None, ticker=None):
        super(Sentimental_Widget, self).__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout(self)

        for ticker in TICKERS:
            item = self.get_widget_items(ticker)
            layout.addWidget(item)

    def get_widget_items(self, tick):
        widget = Sentimental_Widget_Item()
        widget.set_sentimental_ui(ticker=tick)
        return widget


class Sentimental_Widget_Item(QtWidgets.QWidget, Ui_Sentiment_Form):
    def __init__(self, parent=None):
        super(Sentimental_Widget_Item, self).__init__(parent=parent)
        self.setupUi(self)

    def set_sentimental_ui(self, ticker):
        sentiment = self.get_sentiments(ticker)
        prc = LVLS[sentiment['RECOMMENDATION']]
        compagny_name = utils.get_compagny_name_from_tick(ticker)

        self.horizontalSlider.setValue(prc)
        self.horizontalSlider.setEnabled(False)
        self.label.setText(compagny_name)
        self.label.setFont(QtGui.QFont("Times", 12))

    def get_sentiments(self, tick):
        """This method get the Sentiment from the Sentimentals Class
        """
        sentiment = Sentimentals(tick)
        sentiment = sentiment.get_senti()
        return sentiment


class Sentimentals(object):
    """
    This is returning the sentiment for a compagny.
    Going on TradingView, look for indicator if it s a buying, selling or neutral.

    :return: {'RECOMMENDATION': 'BUY', 'BUY: 15, 'SELL': 6, 'NEUTRAL': 4}
    """

    def __init__(self, ticker):
        self.handler = TA_Handler()

        # IF
        ticker = utils.check_french_ticker(ticker)

        country, screener = self.handler.get_screener_from_symabol(ticker)

        self.handler.set_symbol_as(ticker)
        self.handler.set_screener_as_stock(country)
        self.handler.set_exchange_as_crypto_or_stock(screener)
        self.handler.set_interval_as(Interval.INTERVAL_1_DAY)

    def get_senti(self):
        return self.handler.get_analysis().summary


if __name__ == '__main__':
    ticker = "FP.PA"
    x = Sentimentals(ticker=ticker)
    print(x.get_senti())
