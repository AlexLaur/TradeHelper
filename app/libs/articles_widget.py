import webbrowser
from PySide2 import QtWidgets, QtGui
from libs.thread_pool import ThreadPool
from libs.articles.get_articles import Articles


class ArticlesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, ticker=None):
        super(ArticlesWidget, self).__init__(parent)

        self.thread_pool = ThreadPool()
        # self.get_articles(ticker)

    def get_articles(self, ticker):
        if ticker:
            articles = self._get_articles_dict(ticker=ticker).articles

        else:
            # Remplacer par 2 3 ticker Random
            articles = self._get_articles_dict(ticker="GLE").articles

        scroll = QtWidgets.QScrollArea(self)
        widget = QtWidgets.QWidget()
        container = QtWidgets.QVBoxLayout(widget)

        for i in articles:
            title = i["title"]
            date = i["date"]
            description = i["descritpion"]
            link = i["link"]
            article = ArticlesWidgetItem(
                parent=self,
                title=title,
                date=date,
                description=description,
                link=link,
            )
            container.addWidget(article)

        widget.setLayout(container)
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)

    def _get_articles_dict(self, ticker):
        return Articles(ticker=ticker)


class ArticlesWidgetItem(QtWidgets.QWidget):
    def __init__(
        self, parent=None, title=None, date=None, description=None, link=None
    ):
        super(ArticlesWidgetItem, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName(u"layout")
        self.title = LabelTitle(title, link)
        self.title.setObjectName(u"title")
        self.layout.addWidget(self.title)

        self.date = QtWidgets.QLabel(self)
        self.date.setObjectName(u"date")
        self.date.setText(date)
        self.date.setFont(QtGui.QFont("Times", 10))
        self.layout.addWidget(self.date)

        self.description = Description(description)
        self.description.setObjectName(u"description")
        self.description.setEnabled(True)
        self.layout.addWidget(self.description)

        self.spliter = QHLine()
        self.layout.addWidget(self.spliter)


class QHLine(QtWidgets.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


class LabelTitle(QtWidgets.QLabel):
    def __init__(self, text, link=None):
        super(LabelTitle, self).__init__()
        self.link = link

        if text:
            self.setText(text)
            self.setFont(QtGui.QFont("Times", 20))

    def mousePressEvent(self, event) -> None:
        webbrowser.open(self.link)


class Description(QtWidgets.QTextBrowser):
    def __init__(self, text):
        super(Description, self).__init__()
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        if text:
            self.setText(text)
            self.setFont(QtGui.QFont("Times", 10))
