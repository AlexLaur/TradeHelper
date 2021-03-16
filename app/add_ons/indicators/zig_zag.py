import pyqtgraph as pg
import numpy as np

from scipy import signal

from libs.indicators_widget import Indicator


class ZigZag(Indicator):
    def __init__(self):
        super(ZigZag, self).__init__()

        self.name = "ZigZag"
        self.description = ""

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        zigzag = zig_zag(values=values["Close"].values)
        plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index[zigzag]],
            y=values["Close"].values[zigzag],
            pen=pg.mkPen((33, 150, 243), width=2.5),
        )
        self._plots.append(plot)


def zig_zag(values, distance=2.1):
    peaks_up, _ = signal.find_peaks(values, prominence=1, distance=distance)
    peaks_down, _ = signal.find_peaks(-values, prominence=1, distance=distance)

    indexes = [i for i in peaks_up]
    indexes.extend([i for i in peaks_down])
    indexes.sort()

    return np.asarray(indexes)
