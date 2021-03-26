#
# This class set the default Welcome Page.
#

import random
from utils import utils
from PySide2 import QtWidgets
from libs.widgets.stackedwidget import StackedWidget
from libs.articles.yahoo_articles import ArticlesYahoo
from libs.widgets.article_itemwidget import ArticlesWidgetItem


class WelcomeWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__(parent)

        # articles = []
        # for tick in self.rdm_tickers():
        #     artic = self._get_articles_dict(ticker=tick).articles
        #     articles.extend(artic)
        #
        # for index, i in enumerate(articles):
        #     article = ArticlesWidgetItem(parent=self)
        #     article.set_title(i["title"], i["link"])
        #     article.set_compagny(i["compagny"])
        #     article.set_date(i["published"])
        #     article.set_description(i["summary"])
        #     article.set_thumbnail(i["img"])
        #     item = QtWidgets.QListWidgetItem()
        #     item.setSizeHint(article.sizeHint())
        #     self.addItem(item)
        #     self.setItemWidget(item, article)

    def _get_articles_dict(self, ticker):
        return ArticlesYahoo(ticker=ticker, translate=False, single=True)

    def rdm_tickers(self):
        """
        This method select 5 randoms tickers.
        """
        all_tickers = utils.get_all_tickers().keys()
        tickers = random.sample(all_tickers, 5)
        return tickers