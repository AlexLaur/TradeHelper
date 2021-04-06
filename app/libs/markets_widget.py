
import numpy as np
from ui import markets_widget
from PySide2 import QtWidgets
from libs.yahoo_fin import stock_info
from libs.widgets.stackedwidget import StackedWidget

TICKERS = {
    "NASDAQ": "%5EIXIC",
    "S&P 500": "%5EGSPC",
    "Dow Jones": "%5EDJI",
    "Oil": "CL%3DF",
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "EUR/USD": "EURUSD%3DX",
    "GBP/USD": "GBPUSD%3DX",
    "Gold": "GC%3DF",
}

class MarketsWidget(StackedWidget):
    """
    Markets are the informations in the Welcome Page showing price and
    variation from day before.
    """
    def __init__(self, parent=None):
        super(MarketsWidget, self).__init__(parent)

        page = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(page)

        for count, (name, tick) in enumerate(TICKERS.items()):
            if count % 5 == 0:
                page = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(page)
            item = MarketsWidgetItem(self, ticker=tick, compagny=name)
            layout.addWidget(item)

            self.addWidget(page)


class MarketsWidgetItem(QtWidgets.QWidget, markets_widget.Ui_markets):
    def __init__(self, parent=None, ticker=None, compagny=None):
        super(MarketsWidgetItem, self).__init__(parent)

        self.setupUi(self)
        try:
            x = stock_info.get_data(ticker)
        except:
            return

        day = float(x['adjclose'][-1])
        prev_day = float(x['adjclose'][-2])

        if np.isnan(prev_day):
            if not np.isnan(x['adjclose'][-3]):
                prev_day = float(x['adjclose'][-3])
            else:
                prev_day = float(x['adjclose'][-4])

        variation = ((day - prev_day) / prev_day) * 100
        variation = round(variation, 2)

        self.title.setText(compagny)
        self.price.setText("{} €".format(str(round(day, 2))))
        self.pourcentage.setText("{}%".format(str(variation)))

        if variation <= 0:
            self.pourcentage.setStyleSheet("color:rgb(239, 83, 80);")
        else:
            self.pourcentage.setStyleSheet("color:rgb(38, 166, 154);")



