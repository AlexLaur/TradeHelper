import yfinance as yf

from PySide2 import QtWidgets
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        company = yf.Ticker("GLE.PA")
        data = company.history(period="1y", interval="1wk", start="2018-01-01")

        # Remove NaN
        data["Close"] = data["Close"].fillna(data["Close"].mean())

        # plot data: x, y values
        indexes = [i for i, _ in enumerate(data.index)]
        self.graphWidget.plot(indexes, list(data["Close"].values))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()