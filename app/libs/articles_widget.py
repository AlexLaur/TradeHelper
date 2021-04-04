#
# This class set all the articles from a selected compagny.
#

from pprint import pprint
from PySide2 import QtWidgets, QtCore
from libs.articles.yahoo_articles import ArticlesYahoo
from libs.widgets.article_itemwidget import ArticlesWidgetItem


class ArticlesWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None, ticker=None):
        super(ArticlesWidget, self).__init__(parent)
        # self._on_get_articles(ticker)

    @QtCore.Slot(str)
    def _on_get_articles(self, ticker):
        articles = self._get_articles_dict(ticker=ticker)
        self.clear()

        for index, i in enumerate(articles):
            article = ArticlesWidgetItem(parent=self)
            article.set_title(i["title"], i["link"])
            article.set_compagny(i["compagny"])
            article.set_date(i["published"])
            article.set_description(i["summary"])
            article.set_thumbnail(i["img"])
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(article.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, article)


    def _get_articles_dict(self, ticker):
        article = ArticlesYahoo()
        return article.get_articles_from_compagny(ticker=ticker)


