import os
import json
import random
from PySide2 import QtWidgets, QtCore
from libs.thread_pool import ThreadPool
from libs.articles.get_articles import Articles
from libs.widgets.article_itemwidget import ArticlesWidgetItem


SCRIPT_PATH = os.path.dirname(os.path.dirname(__file__))


def read_data():
    """Temp function to load all tickers. Should be loaded by a request in the future"""
    data = {}
    with open(os.path.join(SCRIPT_PATH, "data", "dataset.json"), "r") as f:
        data = json.load(f)
    return data

class WelcomeWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__(parent)

        articles = []
        for tick in self.rdm_tickers():
            artic = self._get_articles_dict(ticker=tick).articles
            if artic:
                articles.append(artic[0])

        for index, i in enumerate(articles):
            title = i["title"]
            date = i["date"]
            description = i["descritpion"]
            link = i["link"]
            article = ArticlesWidgetItem(
                parent=self
            )
            article.set_title(title)
            article.set_date(date)
            article.set_description(description)
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(article.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, article)

    def _get_articles_dict(self, ticker):
        return Articles(ticker=ticker)

    def rdm_tickers(self):
        all_tickers = read_data().keys()
        tickers = random.sample(all_tickers, 5)
        return tickers