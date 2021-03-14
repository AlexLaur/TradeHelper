from PySide2 import QtCore, QtGui, QtWidgets

from utils import utils
from ui.company_widget import Ui_CompanyWidget


class CompanyWidget(QtWidgets.QWidget, Ui_CompanyWidget):
    def __init__(self, parent=None):
        super(CompanyWidget, self).__init__(parent)

        self.setupUi(self)

        # Constants
        self.browser = QtGui.QDesktopServices()

        # Signals
        self.pub_company_logo.clicked.connect(self.open_company_website)

    @QtCore.Slot(dict)
    def _on_ticker_infos(self, infos):
        """Called when infos about the ticker are available

        :param infos: Informations about the ticker
        :type infos: dict
        """
        # TODO need to pass this in a thread

        short_name = infos.get("shortName", None)
        market_price = infos.get("regularMarketPrice", None)
        industry = infos.get("industry", None)
        currency = infos.get("currency", None)
        company_logo_url = infos.get("logo_url", None)
        website = infos.get("website", None)

        open_value = infos.get("regularMarketOpen", None)
        previous_close = infos.get("regularMarketPreviousClose", None)
        day_high = infos.get("regularMarketDayHigh", None)
        day_low = infos.get("regularMarketDayLow", None)
        volume = infos.get("regularMarketVolume", None)

        last_dividend_value = infos.get("lastDividendValue", None)
        last_dividend_date = infos.get("lastDividendDate", None)
        dividend_value = infos.get("dividendRate", None)

        self.lab_company_name.setText(short_name)
        self.lab_market_price.setText(str(market_price))
        self.lab_company_industry.setText(industry)
        self.lab_currency.setText(currency)
        self.pub_company_logo.url = website

        self.lab_open_value.setText(str(open_value))
        self.lab_previous_close_value.setText(str(previous_close))

        self.lab_market_day_high_value.setText(str(day_high))
        self.lab_market_day_low_value.setText(str(day_low))

        self.lab_volume_value.setText(str(volume))

        self.lab_last_dividend_value.setText(str(last_dividend_value))
        self.lab_dividend_value.setText(str(dividend_value))

        if last_dividend_date:
            last_dividend_date = utils.convert_timestamp_to_date(
                timestamp=last_dividend_date
            )
            self.lab_last_dividend_date_value.setText(
                str(last_dividend_date.date())
            )
        else:
            self.lab_last_dividend_date_value.setText(str(last_dividend_date))

        if company_logo_url:
            image = utils.get_image_from_url(url=company_logo_url)

            self.pub_company_logo.setIcon(QtGui.QIcon(image))

    def open_company_website(self):
        """Open the company website in the browser"""
        if getattr(self.pub_company_logo, "url", None):
            self.browser.openUrl(self.pub_company_logo.url)
