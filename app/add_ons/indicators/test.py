import numpy as np
import pyqtgraph as pg

from libs.indicators_widget import Indicator


class ROI(Indicator):
    def __init__(self):
        super(ROI, self).__init__()

        self.name = "ROI"
        self.description = ""

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # roi = pg.LineSegmentROI([[10, 64], [120,64]], pen='r', removable=True)
        # quotation_plot.addItem(roi)

        test = pg.PolyLineROI([[10, 64], [120, 64]], pen="r")
        quotation_plot.addItem(test)
