import yfinance as yf

from PySide2 import QtWidgets
import pyqtgraph as pg

from utils import utils
from utils import candlestick

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, title, values, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.values = values

        self.setWindowTitle(title)

        self.graph_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.graph_widget)

        self.quotation_graph = None
        self.rsi_graph = None

    def candlestick(self, data):
        """
        This function convert the Dataframe into a tuple:
        (index, Open, Close, High, Low)
        :param data:
        :return:
        """
        ls_data = []
        for index, i in enumerate(data.values):
            tuple_data = (index,
                          data['Open'][index],
                          data['Close'][index],
                          data['High'][index],
                          data['Low'][index]
                          )
            ls_data.append(tuple_data)
        item = candlestick.CandlestickItem(ls_data)
        self.quotation_graph.addItem(item)

    def draw_quotation(self):
        self.quotation_graph = self.graph_widget.addPlot(row=0, col=0)
        self.quotation_graph.plot(self.values, pen=pg.mkPen('w', width=3))

    def draw_rsi(self, length=14):
        rsi = utils.get_rsi(values=self.values, length=length)
        self.rsi_graph = self.graph_widget.addPlot(row=1, col=0)
        self.rsi_graph.showGrid(x=True, y=True, alpha=1)

        self.rsi_graph.plot(rsi, connect="finite")
        self.rsi_graph.plot(
            utils.savgol_filter(rsi, 51), pen=pg.mkPen("b", width=1)
        )

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

    def draw_zig_zag(self, value=None):
        if not self.quotation_graph:
            return

        zigzag = utils.zig_zag(values=value)
        self.quotation_graph.plot(zigzag, value[zigzag], pen=pg.mkPen("g", width=1.2))

    def draw_bollinger_bands(self, values):
        color = (102, 169, 218, 0.3)
        middler, upper, lower = utils.bollinger_bands(values)
        self.quotation_graph.plot(middler,  pen=pg.mkPen(color=(color[0], color[1], color[2]), width=1.2))
        up = self.quotation_graph.plot(upper, pen=pg.mkPen(color=(color[0], color[1], color[2]), width=1.2))
        low = self.quotation_graph.plot(lower, pen=pg.mkPen(color=(color[0], color[1], color[2]), width=1.2))
        fill_bb = pg.FillBetweenItem(curve1=up, curve2=low, brush=pg.mkBrush(color[0], color[1], color[2], 50))
        self.quotation_graph.addItem(fill_bb)

    def draw_macd(self, data):
        self.macd_graph = self.graph_widget.addPlot(row=3, col=0)

        macd_line, signal_line, macd = utils.macd(data['Close'])
        ema9 = utils.ExpMovingAverage(macd, w=9)
        macd_bar = macd-ema9

        # Histogram
        bars = pg.BarGraphItem(x=range(macd.shape[0]),
                               height=macd_bar,
                               width=1,
                               brush='r')

        self.macd_graph.plot(ema9, pen=pg.mkPen('r', width=3))
        self.macd_graph.plot(macd, pen=pg.mkPen('b', width=3))
        self.macd_graph.addItem(bars)
        self.macd_graph.setMaximumHeight(150)
        self.macd_graph.showGrid(x=True, y=True, alpha=1)

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
    main.candlestick(data)
    # Draw supports and resistances
    main.draw_supports(closest=0.8)
    main.draw_resistances(closest=0.8)
    # Draw MVA (rolling mean)
    main.draw_mva(lengths=[3, 5, 8, 10, 12, 15])
    # Draw ZigZag
    main.draw_zig_zag(value=values)
    # Draw Bollinger Bands
    main.draw_bollinger_bands(data)
    # Draw RSI (Relative Strength Index)
    # main.draw_rsi()
    # Show window
    main.show()

    app.exec_()
