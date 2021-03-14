import numpy as np
import pyqtgraph as pg

from libs.indicators_widget import Indicator


class MMA(Indicator):
    def __init__(self):
        super(MMA, self).__init__()

        self.name = "Moving Average (3, 5, 8, 10, 12, 15)"
        self.description = "Multiple Moving Average (MMA)"

        # Define args
        self.lengths = [
            {"value": 3, "color": [51, 153, 255], "width": 2},
            {"value": 5, "color": [0, 138, 230], "width": 1.8},
            {"value": 8, "color": [0, 138, 230], "width": 1.6},
            {"value": 10, "color": [0, 138, 230], "width": 1.4},
            {"value": 12, "color": [0, 138, 230], "width": 1.2},
            {"value": 15, "color": [0, 138, 230], "width": 1},
        ]

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        for length in self.lengths:
            mva = mva = values['close'].ewm(com=length["value"]).mean()
            plot = quotation_plot.plot(
                x=[x.timestamp() for x in values.index],
                y=mva,
                connect="finite",
                pen=pg.mkPen(length["color"], width=length["width"]),
            )
            self._plots.append(plot)


class GuppyMMA(Indicator):
    def __init__(self):
        super(GuppyMMA, self).__init__()

        self.name = (
            "Guppy MMA (3, 5, 8, 10, 12, 15) and (30, 35, 40, 45, 50, 60)"
        )
        self.description = "Guppy Multiple Moving Average (GMMA)"

        # Define args
        self.lengths = [
            {"value": 3, "color": [51, 153, 255], "width": 2},
            {"value": 5, "color": [0, 138, 230], "width": 1.8},
            {"value": 8, "color": [0, 138, 230], "width": 1.6},
            {"value": 10, "color": [0, 138, 230], "width": 1.4},
            {"value": 12, "color": [0, 138, 230], "width": 1.2},
            {"value": 15, "color": [0, 138, 230], "width": 1},
            {"value": 30, "color": [51, 153, 255], "width": 2},
            {"value": 35, "color": [179, 36, 0], "width": 1.8},
            {"value": 40, "color": [255, 0, 0], "width": 1.6},
            {"value": 45, "color": [255, 0, 0], "width": 1.4},
            {"value": 50, "color": [255, 0, 0], "width": 1.2},
            {"value": 60, "color": [255, 255, 255], "width": 2},
        ]

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        for length in self.lengths:
            mva = mva = values['close'].ewm(com=length["value"]).mean()
            plot = quotation_plot.plot(
                x=[x.timestamp() for x in values.index],
                y=mva,
                connect="finite",
                pen=pg.mkPen(length["color"], width=length["width"]),
            )
            self._plots.append(plot)


def rolling_mean(values, length):
    """Find the rolling mean for the given data dans the given length

    :param values: All values to analyse
    :type values: np.array
    :param length: The length to calculate the mean
    :type length: int
    :return: The rolling mean
    :rtype: np.array
    """
    ret = np.cumsum(values, dtype=float)
    ret[length:] = ret[length:] - ret[:-length]
    mva = ret[length - 1 :] / length

    # Padding
    padding = np.array([np.nan for i in range(length)])
    mva = np.append(padding, mva)

    return mva
