import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class Panetta(SiteImmo):
    def __init__(self):
        SiteImmo.__init__(self, url.PANETTA_URL)

    def get_links(self):
        param = 'offer/search/transaction/by/city/longwy/property_type/g/max_price/250000/currentPage/1'
        response = requests.get(url=self.url+param, headers=self.headers)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'class': 'detail', 'href': re.compile("^/vente/terrain/meurthe-et-moselle/")}):
            links.append(url.PANETTA_URL + link.get('href')[1:])
        return set(links)
