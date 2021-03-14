import pyqtgraph as pg
import numpy as np
from pprint import pprint
from scipy import signal

from libs.indicators_widget import Indicator

class NonScientific(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super(NonScientific, self).__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [int(value*1) for value in values] #This line return the NonScientific notation value

class Volume(Indicator):
    def __init__(self):
        super(Volume, self).__init__()

        self.name = "Volume"
        self.description = ""

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        self.g_volume = graph_view.addPlot(row=2, col=0, width=1)
        self.g_volume.setMaximumHeight(150)
        self.g_volume.setXLink("Quotation")

        bars = pg.BarGraphItem(
            x=[x.timestamp() for x in values.index],
            height=values['volume'].values,
            width=1,
            brush='r'
        )
        self.g_volume.addItem(bars)
        self.set_time_x_axis(self.g_volume)
        self.g_volume.setAxisItems({"left": NonScientific(orientation="left")})

    def set_time_x_axis(self, widget):
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})
