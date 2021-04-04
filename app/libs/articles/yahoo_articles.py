#
# This Class get all articles from  selected ticker
# from the Yahoo website.

import requests
from bs4 import BeautifulSoup
from utils import utils
from pprint import pprint
from libs.yahoo_fin import news


class ArticlesYahoo(object):
    def __init__(self):
        super(ArticlesYahoo, self).__init__()

        self.articles = None

    def get_articles_from_compagny(self, ticker):
        self.articles = news.get_yf_rss(ticker)
        compagny = utils.get_compagny_name_from_tick(ticker=ticker)

        if not self.articles:
            return

        for article in self.articles:
            article['compagny'] = compagny
            self.get_thumbnail_link(article)
            article['summary'] = self.cup_long_text(article['summary'])

        return self.articles

    def get_home_articles(self):
        self.articles = news.get_yf_home_rss()

        if not self.articles:
            return

        for article in self.articles:
            article['published'] = article['published'].replace('T', ' ')
            article['summary'] = ""
            try:
                article['img'] = article['media_content'][0]['url']
            except:
                article['img'] = ""


        return self.articles

    def get_thumbnail_link(self, article):
        """
        This method scrap the img url of the article from the website.
        """
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        }
        link = article['link']
        request = requests.get(link, headers=header)
        soup = BeautifulSoup(request.text, "html.parser")

        try:
            img = soup.findAll('img', {"class": "caas-img"})
            img = img[-1]['src']
        except:
            img = None
        article['img'] = img

        return article


    def cup_long_text(self, value):
        """
        This method cut long description.
        return: list.
        """
        len_chart = 180
        if len(value) > len_chart:
            value = "{}...".format(value[0:len_chart])
        return value


if __name__ == '__main__':
    tick = "MSFT"
    x = ArticlesYahoo()
    # articles = x.get_articles_from_compagny(tick)
    articles = x.get_home_articles()
    pprint(articles)
