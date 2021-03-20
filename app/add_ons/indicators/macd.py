import numpy as np
import pyqtgraph as pg

from libs.indicators_widget import Indicator, InputField

from PySide2 import QtCore, QtGui


class MACD(Indicator):
    def __init__(self):
        super(MACD, self).__init__()

        self.name = "MACD"
        self.description = ""

        self.g_macd = None

        # Define and register all customisable settings
        field_volumes = InputField("Volumes", color=(239, 83, 80), width=1)
        field_emaslow = InputField("EMA Low", value=12)
        field_emafast = InputField("EMA Fast", value=26)
        field_ema = InputField("EMA", value=9, color=(255, 106, 0), width=2)
        field_macd = InputField("MACD", color=(0, 148, 255), width=2)
        field_buy = InputField("Buy indicator", color=(175, 0, 0), width=10)
        field_sell = InputField("Sell indicator", color=(0, 201, 80), width=10)
        self.register_fields(
            field_volumes,
            field_emaslow,
            field_emafast,
            field_ema,
            field_macd,
            field_buy,
            field_sell,
        )

    def create_indicator(self, graph_view, *args, **kwargs):
        super(MACD, self).create_indicator(self, graph_view)

        # Get values
        values = graph_view.values
        self.quotation_plot = graph_view.g_quotation

        # Init plot
        self.g_macd = graph_view.addPlot(row=2, col=0, width=1)
        self.g_macd.setMaximumHeight(150)
        self.g_macd.setXLink("Quotation")

        # Retrive settings
        field_ema = self.get_field("EMA")
        field_volumes = self.get_field("Volumes")
        field_macd = self.get_field("MACD")
        field_emaslow = self.get_field("EMA Low")
        field_emafast = self.get_field("EMA Fast")

        # Calculations
        macd_line, signal_line, macd = get_macd(
            values=values["Close"].values,
            w_low=field_emaslow.value,
            w_fast=field_emafast.value,
        )
        ema = exp_moving_average(macd, w=field_ema.value)
        macd_bar = macd - ema

        # Draw plots
        bars = pg.BarGraphItem(
            x=[x.timestamp() for x in values.index],
            height=macd_bar,
            width=field_volumes.width,
            fillOutline=True,
            brush=field_volumes.color,
        )
        self.g_macd.plot(
            x=[x.timestamp() for x in values.index],
            y=ema,
            pen=pg.mkPen(field_ema.color, width=field_ema.width),
        )
        self.g_macd.plot(
            x=[x.timestamp() for x in values.index],
            y=macd,
            pen=pg.mkPen(field_macd.color, width=field_macd.width),
        )

        self.g_macd.addItem(bars)
        self.set_time_x_axis(self.g_macd)

        # Draw MACD stategy
        self.strat_macd(values)

    def remove_indicator(self, graph_view, *args, **kwargs):
        super(MACD, self).remove_indicator(graph_view)
        graph_view.removeItem(self.g_macd)
        self.g_macd = None

    def strat_macd(self, values):
        """Draw the strategy on the quotation plot

        :param values: values from the graph
        :type values: pd.Dataframe
        """
        # Retrive settings
        field_buy = self.get_field("Buy indicator")
        field_sell = self.get_field("Sell indicator")
        field_emaslow = self.get_field("EMA Low")
        field_emafast = self.get_field("EMA Fast")
        field_ema = self.get_field("EMA")

        # Calculations
        buy_sell = MACD_strategy(
            values=values,
            w_ema=field_ema.value,
            w_low=field_emaslow.value,
            w_fast=field_emafast.value,
        )

        # Draw plots
        buy_plot = self.quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=buy_sell["Buy"],
            pen=None,
            symbolBrush=field_buy.color,
            symbol="t",
            symbolSize=field_buy.width,
            name="sell",
        )
        sell_plot = self.quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=buy_sell["Sell"],
            pen=None,
            symbolBrush=field_sell.color,
            symbol="t1",
            symbolSize=field_sell.width,
            name="buy",
        )

        # Registers plots in order to delete them later
        self.register_plots(buy_plot, sell_plot)

    def set_time_x_axis(self, widget):
        """Set the time on the X axis

        :param widget: The widget on which to add time
        :type widget: Plot
        """
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})


def exp_moving_average(values, w):
    weights = np.exp(np.linspace(-1.0, 0.0, w))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode="full")[: len(values)]
    a[:w] = a[w]
    return a


def get_macd(values, w_low=12, w_fast=26):
    emaslow = exp_moving_average(values, w=w_low)
    emafast = exp_moving_average(values, w=w_fast)
    return emaslow, emafast, emafast - emaslow


def MACD_strategy(values, w_ema=9, w_low=12, w_fast=26):
    short_EMA = exp_moving_average(values["Close"], w=w_low)
    long_EMA = exp_moving_average(values["Close"], w=w_fast)
    macd = short_EMA - long_EMA
    signal = exp_moving_average(macd, w=w_ema)
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
