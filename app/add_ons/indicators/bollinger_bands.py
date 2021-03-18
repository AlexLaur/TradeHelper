import pyqtgraph as pg

from libs.indicators_widget import Indicator


class BollingerBands(Indicator):
    def __init__(self):
        super(BollingerBands, self).__init__()

        self.name = "Bollinger Bands"
        self.description = ""

        self.g_filler = None
        self.color = (0, 140, 170, 50)

    def create_indicator(self, graph_view, *args, **kwargs):
        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        middler, upper, lower = bollinger_bands(values)

        middler_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=middler,
            pen=pg.mkPen(color=self.color[0:3], width=1.2),
        )
        upper_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=upper,
            pen=pg.mkPen(color=self.color[0:3], width=1.2),
        )
        lower_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=lower,
            pen=pg.mkPen(color=self.color[0:3], width=1.2),
        )

        self.g_filler = pg.FillBetweenItem(
            curve1=upper_plot, curve2=lower_plot, brush=pg.mkBrush(self.color)
        )

        quotation_plot.addItem(self.g_filler)

        self._plots.extend([lower_plot, middler_plot, upper_plot])

    def remove_indicator(self, graph_view, *args, **kwargs):
        super(BollingerBands, self).remove_indicator(
            graph_view=graph_view, *args, **kwargs
        )
        self.g_filler.setBrush(None)
        self.g_filler = None


def bollinger_bands(values):
    middle_band = values["Close"].rolling(window=20).mean()
    standard_deviation = values["Close"].rolling(window=20).std()

    upper_band = middle_band + standard_deviation * 2
    lower_band = middle_band - standard_deviation * 2

    return middle_band.values, upper_band.values, lower_band.values
