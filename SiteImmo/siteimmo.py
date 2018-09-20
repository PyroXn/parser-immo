from threading import Thread

from goose import Goose


class SiteImmo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.articles = []

    def run(self):
        articles = []
        g = Goose()
        for link in self.get_links():
            articles.append(g.extract(url=link))
        self.articles = articles
