import numpy as np
import pyqtgraph as pg

from libs.indicators_widget import Indicator

from PySide2 import QtCore, QtGui


class MACD(Indicator):
    def __init__(self):
        super(MACD, self).__init__()

        self.name = "MACD"
        self.description = ""

        self.g_macd = None

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        self.quotation_plot = graph_view.g_quotation

        self.g_macd = graph_view.addPlot(row=2, col=0, width=1)
        self.g_macd.setMaximumHeight(150)
        self.g_macd.setXLink("Quotation")

        macd_line, signal_line, macd = get_macd(values["Close"].values)

        ema9 = exp_moving_average(macd, w=9)

        macd_bar = macd - ema9

        # Histogram
        bars = pg.BarGraphItem(
            x=[x.timestamp() for x in values.index],
            height=macd_bar,
            width=1,
            fillOutline=True,
            brush=(239, 83, 80),
        )

        self.g_macd.plot(
            x=[x.timestamp() for x in values.index],
            y=ema9,
            pen=pg.mkPen((255, 106, 0), width=2),
        )
        self.g_macd.plot(
            x=[x.timestamp() for x in values.index],
            y=macd,
            pen=pg.mkPen((0, 148, 255), width=2),
        )
        self.g_macd.addItem(bars)
        self.strat_macd(values)
        self.set_time_x_axis(self.g_macd)

    def strat_macd(self, values):
        buy_sell = MACD_strategy(values)
        self.quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=buy_sell["Buy"],
            pen=None,
            symbolBrush=(175, 0, 0),
            symbol="t",
            symbolSize=10,
            name="sell",
        )
        self.quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=buy_sell["Sell"],
            pen=None,
            symbolBrush=(0, 201, 80),
            symbol="t1",
            symbolSize=10,
            name="achat",
        )

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_macd)
        self.g_macd = None

    def set_time_x_axis(self, widget):
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})


def exp_moving_average(values, w):
    weights = np.exp(np.linspace(-1.0, 0.0, w))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode="full")[: len(values)]
    a[:w] = a[w]
    return a


def get_macd(values):
    emaslow = exp_moving_average(values, w=12)
    emafast = exp_moving_average(values, w=26)
    return emaslow, emafast, emafast - emaslow


def MACD_strategy(values):
    short_EMA = exp_moving_average(values["Close"], w=12)
    long_EMA = exp_moving_average(values["Close"], w=26)
    macd = short_EMA - long_EMA
    signal = exp_moving_average(macd, w=9)
    values["MACD"] = macd
    values["Signal"] = signal
    retournement = buy_sell_macd(values)
    values["Buy"] = retournement[0]
    values["Sell"] = retournement[1]
    return values


def buy_sell_macd(values, offset=0.01):
    offset_up = 1 + offset
    offset_down = 1 - offset
    buy = []
    sell = []
    # if 2 lines cross Flag change
    flag = -1
    ema200 = values["Close"].ewm(com=200).mean()

    for i in range(0, len(values)):
        if (
            values["MACD"][i] > values["Signal"][i]
        ):  # and values['close'][i] > ema200[i]:
            sell.append(np.nan)
            if flag != 1:
                buy.append(values["Close"][i] * offset_up)
                flag = 1
            else:
                buy.append(np.nan)

        elif (
            values["MACD"][i] < values["Signal"][i]
        ):  # and values['close'][i] < ema200[i]:
            buy.append(np.nan)
            if flag != 0:
                sell.append(values["Close"][i] * offset_down)
                flag = 0
            else:
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    return (buy, sell)
