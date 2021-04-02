import pyqtgraph as pg
from PySide2 import QtCore, QtGui, QtWidgets

from libs.graph.candlestick import CandlestickItem
from utils import utils

# TODO import from palette or Qss
color = (53, 53, 53)
pg.setConfigOption("background", color)
pg.setConfigOptions(antialias=True)


class GraphView(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None):
        super(GraphView, self).__init__(parent=parent)

        # Constants
        self.values = None
        self.v_line = None
        self.h_line = None

        self.g_quotation = self.addPlot(row=0, col=0, name="Quotation")
        self.g_quotation.showGrid(x=True, y=True, alpha=0.3)
        self.g_vb = self.g_quotation.vb

        self.set_cross_hair()

    def plot_quotation(self, data, clear=True):
        """Plot the quotation

        :param data: The data to plot
        :type data: pd.dataframe
        :param clear: Clear the graph before plot, defaults to True
        :type clear: bool, optional
        """
        self.values = data
        if clear:
            self.g_quotation.clear()
        ls_data = []
        dates = [x.timestamp() for x in data.index]
        for index, (_time, _open, _close, _high, _low) in enumerate(
            zip(
                data.index,
                data["Open"].values,
                data["Close"].values,
                data["High"].values,
                data["Low"].values,
            )
        ):
            ls_data.append((dates[index], _open, _close, _high, _low))
        item = CandlestickItem(ls_data)
        self.g_quotation.addItem(item)
        self.g_quotation.enableAutoRange()

        color_line = (38, 166, 154)
        if data['Close'].iloc[-1] < data['Open'].iloc[-1]:
            color_line = (239, 83, 80)

        self.h_price = pg.InfiniteLine(
            pos=data['Close'].iloc[-1],
            angle=0,
            movable=False,
            pen=pg.mkPen(
                color=color_line,
                width=1,
                style=QtCore.Qt.DotLine,
            ),
        )
        self.g_quotation.addItem(self.h_price, ignoreBounds=True)

        self.set_time_x_axis(widget=self.g_quotation)
        self._set_y_axis_(widget=self.g_quotation, data_close=data['Close'])
        self.set_cross_hair()

    def set_cross_hair(self):
        """Set the cross hair"""
        color = (200, 200, 200)
        label_opts = {
            "position": 0.95,
            "color": color,
            "movable": True,
            "fill": (74, 74, 74),
        }
        pen = pg.mkPen(color, width=1, style=QtCore.Qt.DashLine)
        self.v_line = pg.InfiniteLine(angle=90, movable=False, pen=pen)
        self.h_line = pg.InfiniteLine(
            angle=0,
            movable=False,
            label="{value:0.3f}",
            labelOpts=label_opts,
            pen=pen,
        )
        self.g_quotation.addItem(self.v_line, ignoreBounds=True)
        self.g_quotation.addItem(self.h_line, ignoreBounds=True)
        self.g_quotation.scene().sigMouseMoved.connect(self._on_mouse_moved)

    def set_time_x_axis(self, widget):
        widget.setAxisItems({"bottom": pg.DateAxisItem(orientation="bottom")})

    def _on_mouse_moved(self, event):
        """Signal on mouse moved

        :param event: Mouse position
        :type event: QtCore.QPointF
        """
        sender = self.sender()
        if self.g_quotation.sceneBoundingRect().contains(event):
            mousePoint = self.g_vb.mapSceneToView(event)
            self.v_line.setPos(mousePoint.x())
            self.h_line.setPos(mousePoint.y())

    def _set_y_axis_(self, widget, data_close):
        """Set Y Axis in Left and add Price.

        :param widget: GraphWidget
        :type widget: PQQt.GraphWidget
        :param data_close: Data Price 'Close'
        :type data_close: DataFrame
        """
        widget.showAxis('right')
        axis = widget.getAxis('right')
        axis.setTicks([[(data_close[-1], str(round(data_close[-1], 2)))]])

    # def mouseMoveEvent(self, event):
    #     print(event.pos())



class GraphWidget(QtWidgets.QWidget):
    """Widget wrapper for the graph"""

    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent=parent)

        layout = QtWidgets.QHBoxLayout()
        self._graph = GraphView(parent=self)
        layout.addWidget(self._graph)
        self.setLayout(layout)

    @property
    def graph(self):
        """Return the graph

        :return: The graph view
        :rtype: GraphView object
        """
        return self._graph

    def draw_resistance(self, *args, **kwargs):
        print("hello")
