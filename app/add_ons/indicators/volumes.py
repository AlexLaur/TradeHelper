import pyqtgraph as pg
import numpy as np
from pprint import pprint
from scipy import signal

from libs.graph.bargraph import BarGraphItem
from utils.indicators_utils import Indicator, InputField


class NonScientific(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(NonScientific, self).__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [
            int(value * 1) for value in values
        ]  # This line return the NonScientific notation value


class Volumes(Indicator):
    def __init__(self):
        super(Volumes, self).__init__()

        self.name = "Volumes"
        self.description = ""

        self.g_volume = None

        # Define and register all customisable settings
        field_up = InputField(
            "Upper", color=(38, 166, 154), disable_line_style=True
        )
        field_low = InputField(
            "Lower", color=(239, 83, 80), disable_line_style=True
        )
        self.register_fields(field_up, field_low)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(Volumes, self).create_indicator(graph_view)

        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # Retrive settings
        field_up = self.get_field("Upper")
        field_low = self.get_field("Lower")

        # Draw plots
        self.g_volume = graph_view.addPlot(
            row=3, col=0, width=1, title="<b>{name}</b>".format(name=self.name)
        )
        self.g_volume.setAxisItems({"left": NonScientific(orientation="left")})
        self.g_volume.setMaximumHeight(150)
        self.g_volume.setXLink("Quotation")
        self.g_volume.setLimits(yMin=0)

        bars = BarGraphItem(
            x=[x.timestamp() for x in values.index],
            height=values["Volume"].values,
            up_color=field_up.color,
            down_color=field_low.color,
            previous_offset=True,
        )
        self.g_volume.addItem(bars)

        self.set_time_x_axis(self.g_volume)

    def remove_indicator(self, graph_view, *args, **kwargs):
        graph_view.removeItem(self.g_volume)
        self.g_volume = None

    def set_time_x_axis(self, widget):
        """Set the time on the X axis

        :param widget: The widget on which to add time
        :type widget: Plot
        """
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})
