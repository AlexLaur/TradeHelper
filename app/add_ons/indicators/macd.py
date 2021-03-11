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
        quotation_plot = graph_view.g_quotation

        self.g_macd = graph_view.addPlot(row=2, col=0, width=1)
        self.g_macd.setMaximumHeight(150)
        self.g_macd.setXLink("Quotation")

        macd_line, signal_line, macd = get_macd(values["Close"].values)

        ema9 = exp_moving_average(macd, w=9)

        macd_bar = macd - ema9

        # Histogram
        bars = pg.BarGraphItem(
            x=range(macd.shape[0]),
            height=macd_bar,
            width=1,
            fillOutline=True,
            brush=(239, 83, 80),
        )

        self.g_macd.plot(ema9, pen=pg.mkPen((255, 106, 0), width=2))
        self.g_macd.plot(macd, pen=pg.mkPen((0, 148, 255), width=2))
        self.g_macd.addItem(bars)

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_macd)
        self.g_macd = None


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
