import numpy as np
import pyqtgraph as pg

from utils.indicators_utils import Indicator, InputField, ChoiceField

RATIO = [78.6, 61.8, 50.0, 38.2, 23.6]
COLORS = {
            78.6: (255, 56, 56),
            61.8: (218, 255, 56),
            50.0: (56, 255, 82),
            38.2: (148, 56, 255),
            23.6: (56, 95, 255),
        }

class Fibonnaci(Indicator):
    def __init__(self):
        super(Fibonnaci, self).__init__()

        self.name = "Fibonnaci"
        self.description = "Fibonnaci"

        # Define and register all customisable settings
        # field_input = ChoiceField(
        #     "Input", choices=["Open", "Close", "High", "Low"], default="Close"
        # )
        # self.register_field(field_input)
        # line1 = InputField(
        #     "Fibonnaci", color=(51, 153, 255), value=3, width=2
        # )
        # self.register_fields(line1)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(Fibonnaci, self).create_indicator(self, graph_view)

        # Get values
        values = graph_view.values
        self.quotation_plot = graph_view.g_quotation

        self.roi = pg.RectROI([347, 113], [50, 60],
                              invertible=True,
                              pen=pg.mkPen(color=(255, 255, 255),
                                           width=1,),
                              hoverPen=None,
                              )

        self.roi.addTranslateHandle((0,0))
        self.quotation_plot.addItem(self.roi)

        self.set_fibonnaci_levels()
        self.roi.sigRegionChanged.connect(self.move_items)

    def move_items(self):
        """This method is call everytime the ROI is move.
        """
        self.set_fibonnaci_levels()

    def set_fibonnaci_levels(self):
        try:
            self.quotation_plot.removeItem(self.line_78)
            self.quotation_plot.removeItem(self.label_78)
            self.quotation_plot.removeItem(self.line_61)
            self.quotation_plot.removeItem(self.label_61)
            self.quotation_plot.removeItem(self.line_50)
            self.quotation_plot.removeItem(self.label_50)
            self.quotation_plot.removeItem(self.line_38)
            self.quotation_plot.removeItem(self.label_38)
            self.quotation_plot.removeItem(self.line_23)
            self.quotation_plot.removeItem(self.label_23)
            self.quotation_plot.removeItem(self.label_1)
            self.quotation_plot.removeItem(self.label_100)
        except:
            pass

        self.line_78 = self._set_fibonnaci_level(prc=78.6)
        self.label_78 = self._set_label_level(prc=78.6)

        self.line_61 = self._set_fibonnaci_level(prc=61.8)
        self.label_61 = self._set_label_level(prc=61.8)

        self.line_50 = self._set_fibonnaci_level(prc=50.0)
        self.label_50 = self._set_label_level(prc=50.0)

        self.line_38 = self._set_fibonnaci_level(prc=38.2)
        self.label_38 = self._set_label_level(prc=38.2)

        self.line_23 = self._set_fibonnaci_level(prc=23.6)
        self.label_23 = self._set_label_level(prc=23.6)

        self.label_100 = self._set_label_level(prc=100)
        self.label_1 = self._set_label_level(prc=1)

        self.quotation_plot.addItem(self.line_78)
        self.quotation_plot.addItem(self.label_78)
        self.quotation_plot.addItem(self.line_61)
        self.quotation_plot.addItem(self.label_61)
        self.quotation_plot.addItem(self.line_50)
        self.quotation_plot.addItem(self.label_50)
        self.quotation_plot.addItem(self.line_38)
        self.quotation_plot.addItem(self.label_38)
        self.quotation_plot.addItem(self.line_23)
        self.quotation_plot.addItem(self.label_23)
        self.quotation_plot.addItem(self.label_100)
        self.quotation_plot.addItem(self.label_1)

    def _set_fibonnaci_level(self, prc=50.0):
        """This method plot line for each retracement
        :param widget: ROIWidget
        :type widget: PQQt.GraphWidget
        """
        color = COLORS[prc]
        xpos, ypos = self.position_line(prc)

        line = pg.LineSegmentROI(positions=(xpos, ypos),
                                 pen=pg.mkPen(color, width=2),
                                 movable=False,
                                 rotatable=False,
                                 resizable=False,
                                 )
        line.setSelected(False)
        return line


    def _set_label_level(self, prc=50.0):
        """This method plot label for each retracement
        :param widget: TextItem
        :type widget: PQQt.GraphWidget
        """
        xpos, ypos = self.position_line(prc)

        percentg_lb = "0.{}".format(int(prc))
        label = pg.TextItem(text='  {} ({})'.format(percentg_lb, round(ypos[1], 2)),
                            anchor=(0, 0.5),
                            )

        # Lock Label to the Right of ROI
        if xpos[0] < ypos[0]:
            position = ypos[0]
        else:
            position = xpos[0]

        label.setPos(position, ypos[1])
        return label

    def position_line(self, prc=50.0):
        """This method return the graph position for the levels
        """
        rtc = self._get_fibonnaci_level(prc)[0]
        x_pos = [self.roi.pos()[0], rtc]
        y_pos = [self.roi.pos()[0] + self.roi.size()[0], rtc]
        return x_pos, y_pos


    def _get_fibonnaci_level(self, prc):
        """This method calcul the retracement level calculating the difference
            between the min/max of the ROI.
            :param prc: Percentage to calculate
            :type float:
        """
        # position is lower-left ROI
        # use x_min and y_min with width and height to find the position
        # on the graph.
        pos = self.roi.getState()['pos']
        size = self.roi.getState()['size']

        y_min = pos[1]
        y_max = pos[1] + size[1]
        variation = y_max - y_min

        retracement = []
        retrc = variation * (prc / 100)
        value = y_min + retrc
        retracement.append(value)

        return retracement

    def remove_indicator(self, graph_view, *args, **kwargs):
        super(Fibonnaci, self).remove_indicator(graph_view)
