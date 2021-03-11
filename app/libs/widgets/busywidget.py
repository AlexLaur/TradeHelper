from PySide2 import QtCore, QtGui, QtWidgets, QtSvg

import resources_rc


class BusyIndicator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BusyIndicator, self).__init__(parent)

        self.resize(100, 100)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        layout = QtWidgets.QHBoxLayout()
        svg = QtSvg.QSvgWidget()
        svg.load(u":/svg/tail-spin.svg")
        layout.addWidget(svg)
        self.setLayout(layout)

        self.hide()

    def show(self, center_from=None):
        if center_from:
            self.move(center_from.rect().center() - self.rect().center())
        else:
            self.move(self.parent().rect().center() - self.rect().center())
        super(BusyIndicator, self).show()

    def hide(self):
        super(BusyIndicator, self).hide()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(
            event.rect(), QtGui.QBrush(QtGui.QColor(55, 55, 55, 255))
        )
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        painter.end()
