import yfinance as yf
import numpy as np

from scipy.signal import find_peaks
from statistics import mean
from peakdetect import peakdetect

from PySide2 import QtWidgets
import pyqtgraph as pg

from utils import utils


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle(company.info.get("shortName"))

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # plot data: x, y values
        self.graphWidget.plot(indexes, list(data["Close"].values))

        for i in resistances:
            self.graphWidget.addLine(y=i, pen=pg.mkPen('r', width=1))
        for i in supports:
            self.graphWidget.addLine(y=i, pen=pg.mkPen('g', width=1))

        # Need to move mma to x+lenght
        self.graphWidget.plot(range(len(mma)), mma, pen=pg.mkPen('b', width=1))


if __name__ == '__main__':

    company = yf.Ticker("BN.PA")
    data = company.history(period="1y", interval="1wk", start="2018-01-01")

    # Remove NaN
    data["Close"] = data["Close"].fillna(data["Close"].mean())
    indexes = range(len(data.index))
    values = data["Close"].values


    resistances = utils.get_resistances(values=values)
    supports = utils.get_supports(values=values)
    mma = list(utils.rolling_mean(values, 5))


    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()