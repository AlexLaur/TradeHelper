import pyqtgraph as pg
import pandas as pd

from PySide2 import QtCore

from libs.indicators_widget import Indicator


class RSI(Indicator):
    def __init__(self):
        super(RSI, self).__init__()

        self.name = "RSI 14d (Relative Strength Index 14 days)"
        self.description = ""

        self.g_rsi = None

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        rsi = get_rsi(values=values["Close"].values, length=14)

        self.g_rsi = graph_view.addPlot(row=1, col=0, width=1)
        self.g_rsi.showGrid(x=True, y=True, alpha=1)
        self.g_rsi.setMaximumHeight(150)
        self.g_rsi.setXLink("Quotation")

        plot = self.g_rsi.plot(
            x=[x.timestamp() for x in values.index],
            y=rsi,
            connect="finite",
            pen=pg.mkPen((142, 21, 153), width=1.5),
        )

        # Draw overbought and oversold
        line_up = self.g_rsi.addLine(
            y=70,
            pen=pg.mkPen((200, 200, 200), width=1.5, style=QtCore.Qt.DashLine),
        )
        line_down = self.g_rsi.addLine(
            y=30,
            pen=pg.mkPen((200, 200, 200), width=1.5, style=QtCore.Qt.DashLine),
        )
        self.set_time_x_axis(self.g_rsi)

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_rsi)
        self.g_rsi = None

    def set_time_x_axis(self, widget):
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})


def get_rsi(values, length=14):
    """Relative strength index"""
    # Approximate; good enough
    gain = pd.Series(values).diff()
    loss = gain.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    rs = gain.ewm(length).mean() / loss.abs().ewm(length).mean()
    return (100 - 100 / (1 + rs)).to_numpy()
