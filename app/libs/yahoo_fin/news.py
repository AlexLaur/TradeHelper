import feedparser

yf_rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=FR&lang=fr-FR"
home_page = "https://finance.yahoo.com/news/rssr/2.0/"


def get_yf_rss(ticker):

    feeds = feedparser.parse(yf_rss_url % ticker)

    return feeds.entries


def get_yf_home_rss():

    feeds = feedparser.parse(home_page)

    return feeds.entries