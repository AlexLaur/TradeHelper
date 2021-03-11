import pyqtgraph as pg
from PySide2 import QtCore, QtGui


class CandlestickItem(pg.GraphicsObject):
    def __init__(
        self, data, up_color=(38, 166, 154), down_color=(239, 83, 80)
    ):
        pg.GraphicsObject.__init__(self)

        self.data = data  ## data must have fields: time, open, close, min, max
        self.up_color = up_color
        self.down_color = down_color

        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        w = (self.data[1][0] - self.data[0][0]) / 3.0
        for (t, open, close, min, max) in self.data:
            if open > close:
                p.setPen(pg.mkPen(self.down_color))
                p.setBrush(pg.mkBrush(self.down_color))
            else:
                p.setPen(pg.mkPen(self.up_color))
                p.setBrush(pg.mkBrush(self.up_color))
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
