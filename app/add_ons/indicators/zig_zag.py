import pyqtgraph as pg
import numpy as np

from scipy import signal

from libs.indicators_widget import Indicator, InputField, ChoiceField


class ZigZag(Indicator):
    def __init__(self):
        super(ZigZag, self).__init__()

        self.name = "ZigZag"
        self.description = ""

        # Define and register all customisable settings
        field_input = ChoiceField(
            "Input", choices=["Open", "Close", "High", "Low"], default="Close"
        )
        field_zigzag = InputField("ZigZag", color=(33, 150, 243), width=2.5)
        self.register_fields(field_input, field_zigzag)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(ZigZag, self).create_indicator(graph_view)

        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # Retrive settings
        field_input = self.get_field("Input")
        field_zigzag = self.get_field("ZigZag")

        # Calculation
        zigzag = zig_zag(values=values[field_input.current].values)

        # Draw plot
        plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index[zigzag]],
            y=values[field_input.current].values[zigzag],
            pen=pg.mkPen(
                field_zigzag.color,
                width=field_zigzag.width,
                style=field_zigzag.line_style,
            ),
        )
        self.register_plot(plot)


def zig_zag(values, distance=2.1):
    peaks_up, _ = signal.find_peaks(values, prominence=1, distance=distance)
    peaks_down, _ = signal.find_peaks(-values, prominence=1, distance=distance)

    indexes = [i for i in peaks_up]
    indexes.extend([i for i in peaks_down])
    indexes.sort()

    return np.asarray(indexes)
