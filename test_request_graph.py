import yfinance as yf

from PySide2 import QtWidgets
import pyqtgraph as pg

from utils import utils


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, title, values, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.values = values

        self.setWindowTitle(title)

        self.graph_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.graph_widget)

        self.quotation_graph = None
        self.rsi_graph = None

    def draw_quotation(self):
        self.quotation_graph = self.graph_widget.addPlot(row=0, col=0)
        self.quotation_graph.plot(self.values)

    def draw_rsi(self, length=14):
        rsi = utils.get_rsi(values=self.values, length=length)
        self.rsi_graph = self.graph_widget.addPlot(row=1, col=0)
        self.rsi_graph.showGrid(x=True, y=True, alpha=1)

        self.rsi_graph.plot(rsi, connect="finite")
        self.rsi_graph.plot(utils.savgol_filter(rsi, 51), pen=pg.mkPen("b", width=1))

        # Draw overbought and oversold
        self.rsi_graph.addLine(y=70, pen=pg.mkPen("r", width=2))
        self.rsi_graph.addLine(y=30, pen=pg.mkPen("r", width=2))

    def draw_mva(self, lengths=None):
        if not lengths or not self.quotation_graph:
            return

        for length in lengths:
            mva = utils.rolling_mean(values=self.values, length=length)
            self.quotation_graph.plot(
                mva,
                connect="finite",
                pen=pg.mkPen("b", width=1),
            )

    def draw_resistances(self, closest=None):
        if not self.quotation_graph:
            return

        resistances = utils.get_resistances(
            values=self.values, closest=closest
        )
        for res in resistances:
            self.quotation_graph.addLine(y=res, pen=pg.mkPen("r", width=1))

    def draw_supports(self, closest=None):
        if not self.quotation_graph:
            return

        supports = utils.get_supports(values=self.values, closest=closest)
        for sup in supports:
            self.quotation_graph.addLine(y=sup, pen=pg.mkPen("g", width=1))


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    ticker = yf.Ticker("BN.PA")
    data = ticker.history(period="1y", interval="1d", start="2019-01-01")

    title = ticker.info.get("shortName")
    values = utils.remove_nan(values=data["Close"].values)

    # Main Window
    main = MainWindow(title=title, values=values)
    # Draw the quotations
    main.draw_quotation()
    # Draw supports and resistances
    main.draw_supports(closest=0.8)
    main.draw_resistances(closest=0.8)
    # Draw MVA (rolling mean)
    main.draw_mva(lengths=[3, 5, 8, 10, 12, 15])
    # Draw RSI (Relative Strength Index)
    main.draw_rsi()
    # Show window
    main.show()

    app.exec_()
