import yfinance as yf

from PySide2 import QtWidgets
import pyqtgraph as pg

from utils import utils


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.setWindowTitle(company.info.get("shortName"))

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # plot data: x, y values
        self.graphWidget.plot(range(values.shape[0]), list(values))

        for i in kwargs.get("resistances", []):
            self.graphWidget.addLine(y=i, pen=pg.mkPen('r', width=1))
        for i in kwargs.get("supports", []):
            self.graphWidget.addLine(y=i, pen=pg.mkPen('g', width=1))

        for rolling_mean in kwargs.get("rolling_means", []):
            self.graphWidget.plot(range(len(rolling_mean)), rolling_mean, pen=pg.mkPen('b', width=1))

if __name__ == '__main__':

    resistances = None
    supports = None
    rolling_means = []

    company = yf.Ticker("BN.PA")
    data = company.history(period="1y", interval="1wk", start="2018-01-01")

    values = utils.remove_nan(values=data["Close"].values)


    resistances = utils.get_resistances(values=values, closest=1.2)
    supports = utils.get_supports(values=values, closest=1.2)

    # example of rolling mean
    for lenght in [3, 5, 8, 10, 12, 15]:
        mma = list(utils.rolling_mean(values=values, lenght=lenght))
        rolling_means.append(mma)


    app = QtWidgets.QApplication([])
    main = MainWindow(resistances=resistances, supports=supports, rolling_means=rolling_means)
    main.show()
    app.exec_()
