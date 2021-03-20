import pyqtgraph as pg
import pandas as pd

from PySide2 import QtCore

from libs.indicators_widget import Indicator, InputField


class RSI(Indicator):
    def __init__(self):
        super(RSI, self).__init__()

        self.name = "RSI 14d (Relative Strength Index 14 days)"
        self.description = ""

        self.g_rsi = None

        # Define and register all customisable settings
        field_up = InputField("Up", color=(200, 200, 200), width=1.5)
        field_down = InputField("Down", color=(200, 200, 200), width=1.5)
        field_rsi = InputField(
            "RSI", value=14, color=(142, 21, 153), width=1.5
        )
        self.register_fields(field_up, field_down, field_rsi)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(RSI, self).create_indicator(graph_view)

        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # Retrive settings
        field_up = self.get_field("Up")
        field_down = self.get_field("Down")
        field_rsi = self.get_field("RSI")

        # Calculation
        rsi = get_rsi(values=values["Close"].values, length=field_rsi.value)

        # Draw plots
        self.g_rsi = graph_view.addPlot(
            row=1, col=0, width=1, title="<b>RSI</b>"
        )
        self.g_rsi.showGrid(x=True, y=True, alpha=1)
        self.g_rsi.setMaximumHeight(150)
        self.g_rsi.setXLink("Quotation")

        plot = self.g_rsi.plot(
            x=[x.timestamp() for x in values.index],
            y=rsi,
            connect="finite",
            pen=pg.mkPen(field_rsi.color, width=field_rsi.width),
        )

        # Draw overbought and oversold
        line_up = self.g_rsi.addLine(
            y=70,
            pen=pg.mkPen(
                field_up.color, width=field_up.width, style=QtCore.Qt.DashLine
            ),
        )
        line_down = self.g_rsi.addLine(
            y=30,
            pen=pg.mkPen(
                field_down.color,
                width=field_down.width,
                style=QtCore.Qt.DashLine,
            ),
        )
        self.set_time_x_axis(self.g_rsi)

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_rsi)
        self.g_rsi = None

    def set_time_x_axis(self, widget):
        """Set the time on the X axis

        :param widget: The widget on which to add time
        :type widget: Plot
        """
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
