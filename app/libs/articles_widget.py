import webbrowser
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from libs.articles.get_articles import Articles


class ArticlesWidget(QWidget):
    def __init__(self, parent=None, ticker=None):
        super(ArticlesWidget, self).__init__(parent)
        self.get_articles(ticker)

    def get_articles(self, ticker):
        if ticker:
            _articles = Articles(ticker=ticker)
            articles = _articles.articles

        else:
            # Remplacer par 2 3 ticker Random
            _articles = Articles(ticker='GLE')
            articles = _articles.articles

        scroll = QScrollArea(self)
        widget = QWidget()
        container = QVBoxLayout(widget)

        for i in articles:
            title = i['title']
            date = i['date']
            description = i['descritpion']
            link = i['link']
            article = ArticlesWidgetItem(parent=self,
                                         title=title,
                                         date=date,
                                         description=description,
                                         link=link,
                                         )
            container.addWidget(article)

        widget.setLayout(container)
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)


class ArticlesWidgetItem(QWidget):
    def __init__(self, parent=None, title=None, date=None, description=None, link=None):
        super(ArticlesWidgetItem, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setObjectName(u"layout")
        self.title = LabelTitle(title, link)
        self.title.setObjectName(u"title")
        self.layout.addWidget(self.title)

        self.date = QLabel(self)
        self.date.setObjectName(u"date")
        self.date.setText(date)
        self.date.setFont(QFont('Times', 10))
        self.layout.addWidget(self.date)

        self.description = Description(description)
        self.description.setObjectName(u"description")
        self.description.setEnabled(True)
        self.layout.addWidget(self.description)

        self.spliter = QHLine()
        self.layout.addWidget(self.spliter)


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class LabelTitle(QLabel):
    def __init__(self, text, link=None):
        super(LabelTitle, self).__init__()
        self.link = link

        if text:
            self.setText(text)
            self.setFont(QFont('Times', 20))

    def mousePressEvent(self, event) -> None:
        webbrowser.open(self.link)

class Description(QTextBrowser):
    def __init__(self, text):
        super(Description, self).__init__()
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        if text:
            self.setText(text)
            self.setFont(QFont('Times', 10))