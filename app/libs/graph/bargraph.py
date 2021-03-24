from PySide2 import QtCore, QtGui
import pyqtgraph as pg


class BarGraphItem(pg.GraphicsObject):
    def __init__(
        self,
        x,
        height,
        up_color=(38, 166, 154),
        down_color=(239, 83, 80),
        previous_offset=False,
    ):
        pg.GraphicsObject.__init__(self)

        self.data = []
        for x, y in zip(x, height):
            self.data.append((x, y))

        self.up_color = up_color
        self.down_color = down_color
        self.previous_offset = previous_offset

        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()

        p = QtGui.QPainter(self.picture)
        w = (self.data[1][0] - self.data[0][0]) / 2.5
        previous = 0

        for index, (x, y) in enumerate(self.data):
            if y >= previous:
                p.setPen(pg.mkPen(self.up_color))
                p.setBrush(pg.mkBrush(self.up_color))
            else:
                p.setPen(pg.mkPen(self.down_color))
                p.setBrush(pg.mkBrush(self.down_color))
            if self.previous_offset:
                previous = y
            p.drawRect(QtCore.QRectF(x - w, 0, w * 2, y))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
