import pyqtgraph as pg
import numpy as np
from pprint import pprint
from scipy import signal

from libs.indicators_widget import Indicator, InputField


class NonScientific(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(NonScientific, self).__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [
            int(value * 1) for value in values
        ]  # This line return the NonScientific notation value


class Volume(Indicator):
    def __init__(self):
        super(Volume, self).__init__()

        self.name = "Volume"
        self.description = ""

        self.g_volume = None

        # Define and register all customisable settings
        field_volume = InputField("Volume", color=(255, 0, 0), width=1)
        self.register_field(field_volume)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(Volume, self).create_indicator(graph_view)

        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # Retrive settings
        field_volume = self.get_field("Volume")

        # Draw plots
        self.g_volume = graph_view.addPlot(
            row=3, col=0, width=1, title="<b>Volumes</b>"
        )
        self.g_volume.setAxisItems({"left": NonScientific(orientation="left")})
        self.g_volume.setMaximumHeight(150)
        self.g_volume.setXLink("Quotation")

        bars = pg.BarGraphItem(
            x=[x.timestamp() for x in values.index],
            height=values["Volume"].values,
            width=field_volume.width,
            brush=pg.mkBrush(field_volume.color),
        )

        self.set_time_x_axis(self.g_volume)
        self.g_volume.addItem(bars)

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_volume)
        self.g_volume = None

    def set_time_x_axis(self, widget):
        """Set the time on the X axis

        :param widget: The widget on which to add time
        :type widget: Plot
        """
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})
