import random
from ui import articles as ui
from PySide2 import QtWidgets, QtGui
from libs.thread_pool import ThreadPool
from libs.articles.get_articles import Articles


class ArticlesWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None, ticker=None):
        super(ArticlesWidget, self).__init__(parent)

        self.thread_pool = ThreadPool()
        self.get_articles(ticker)

    def get_articles(self, ticker):
        print(ticker, "wgt_articles")
        if ticker:
            # rdm_tickers = random.sample(,5)

            articles = self._get_articles_dict(ticker=ticker).articles

        else:
            # Remplacer par 2 3 ticker Random
            articles = self._get_articles_dict(ticker="GLE").articles

        for i in articles:
            title = i["title"]
            date = i["date"]
            description = i["descritpion"]
            link = i["link"]

            article = ArticlesWidgetItem(
                parent=self,
            )
            article.set_title(title, link)
            article.set_date(date)
            article.set_description(description)

            article_item = QtWidgets.QListWidgetItem(self)
            article_item.setSizeHint(article.sizeHint())
            self.addItem(article_item)
            self.setItemWidget(article_item, article)


    def _get_articles_dict(self, ticker):
        return Articles(ticker=ticker)


class ArticlesWidgetItem(QtWidgets.QWidget, ui.Ui_Form):
    def __init__(self, parent=None):
        super(ArticlesWidgetItem, self).__init__(parent)
        self.setupUi(self)

    def set_title(self, text, link=None):
        self.title_lb.setText(text)

    def set_date(self, text):
        self.date_lb.setText(text)

    def set_description(self, text):
        self.descri.setText(text)


class QHLine(QtWidgets.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)

