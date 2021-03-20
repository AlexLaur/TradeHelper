import pyqtgraph as pg

from libs.indicators_widget import Indicator, InputField


class BollingerBands(Indicator):
    def __init__(self):
        super(BollingerBands, self).__init__()

        self.name = "Bollinger Bands"
        self.description = ""

        self.g_filler = None

        # Define and register all customisable settings
        field_middle = InputField("Middle", color=(0, 140, 170), width=1.2)
        field_upper = InputField("Upper", color=(0, 140, 170), width=1.2)
        field_lower = InputField("Lower", color=(0, 140, 170), width=1.2)
        field_filler = InputField("Fill Between", color=(0, 140, 170, 50))
        self.register_fields(field_middle, field_upper, field_lower, field_filler)

    def create_indicator(self, graph_view, *args, **kwargs):
        super(BollingerBands, self).create_indicator(graph_view)

        # Get values
        values = graph_view.values
        quotation_plot = graph_view.g_quotation

        # Retrive settings
        field_middle = self.get_field("Middle")
        field_upper = self.get_field("Middle")
        field_lower = self.get_field("Lower")
        field_filler = self.get_field("Fill Between")

        # Calculate
        middler, upper, lower = bollinger_bands(values)

        # Create plots
        middler_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=middler,
            pen=pg.mkPen(color=field_middle.color, width=field_middle.width),
        )

        upper_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=upper,
            pen=pg.mkPen(color=field_upper.color, width=field_upper.width),
        )

        lower_plot = quotation_plot.plot(
            x=[x.timestamp() for x in values.index],
            y=lower,
            pen=pg.mkPen(color=field_lower.color, width=field_lower.width),
        )

        self.g_filler = pg.FillBetweenItem(
            curve1=upper_plot, curve2=lower_plot, brush=pg.mkBrush(field_filler.color)
        )

        quotation_plot.addItem(self.g_filler)
        self._plots.extend([lower_plot, middler_plot, upper_plot])

    def remove_indicator(self, graph_view, *args, **kwargs):
        super(BollingerBands, self).remove_indicator(
            graph_view=graph_view, *args, **kwargs
        )
        self.g_filler.setBrush(None)
        self.g_filler = None


def bollinger_bands(values, window=20):
    middle_band = values["Close"].rolling(window=window).mean()
    standard_deviation = values["Close"].rolling(window=window).std()

    upper_band = middle_band + standard_deviation * 2
    lower_band = middle_band - standard_deviation * 2

    return middle_band.values, upper_band.values, lower_band.values
