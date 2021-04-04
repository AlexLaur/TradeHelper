#
# This class set the default Welcome Page.
#
from pprint import pprint
import random
from utils import utils
from PySide2 import QtWidgets
from libs.articles.yahoo_articles import ArticlesYahoo
from libs.widgets.article_itemwidget import ArticlesWidgetItem


class WelcomeWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(WelcomeWidget, self).__init__(parent)

        articles = self._get_articles_dict()[:5]

        for index, i in enumerate(articles):
            article = ArticlesWidgetItem(parent=self)
            article.set_title(i["title"], i["link"])
            article.set_date(i["published"])
            article.set_description(i["summary"])
            article.set_thumbnail(i["img"])
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(article.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, article)

    def _get_articles_dict(self):
        article = ArticlesYahoo()
        return article.get_home_articles()



