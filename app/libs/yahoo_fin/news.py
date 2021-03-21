import feedparser

yf_rss_url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=FR&lang=fr-FR"


def get_yf_rss(ticker):

    feeds = feedparser.parse(yf_rss_url % ticker)

    return feeds.entries
