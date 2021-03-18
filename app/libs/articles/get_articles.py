import requests
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd
from libs.yahoo_fin import stock_info as sf

from libs import yahoo_fin


class Articles(object):
    def __init__(self, ticker=None):
        super(Articles, self).__init__()

        self.headers = {
            "authority": "www.boursorama.com",
            "method": "GET",
            "path": "/cours/actualites/1rPBN/",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "referer": "https://www.boursorama.com/cours/1rPBN/",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        }
        self.get_url(ticker=ticker)

    def get_url(self, ticker):
        if "{}.PA".format(ticker) in sf.tickers_cac().keys():
            url = "https://www.boursorama.com/cours/actualites/1rP{}/".format(
                ticker
            )
        else:
            url = "https://www.boursorama.com/cours/actualites/{}/".format(
                ticker
            )
        self.response = requests.get(url, headers=self.headers)
        self.soup()

    def soup(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        articles_html = soup.find("article").findAll(
            "li", {"class": "c-list-details-news__line / o-flag"}
        )

        self.articles = []

        for index, i in enumerate(articles_html):
            title = i.find("a").get("title")
            time = i.find("span", {"class": "c-source__time"}).string
            descritpion = i.find(
                "p", {"class": "c-list-details-news__content"}
            ).string.strip()
            link = i.find("a")["href"]
            self.articles.append(
                {
                    "title": title,
                    "date": time,
                    "descritpion": descritpion,
                    "link": "https://www.boursorama.com{}".format(link),
                }
            )

        # pprint(self.articles)


if __name__ == "__main__":
    ticker = "BN"
    # ticker = "KO"
    get = Articles(ticker)
