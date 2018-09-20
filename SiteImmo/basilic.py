import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class Basilic(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.BASILIC_URL + 'liste.php')
        self.parameters = parameters

    def get_links(self):
        payload = {'bien_nature': 'vente',
                   'bien_type[]': self.parameters.type,
                   'bien_pays': 'france',
                   'budget_min': '',
                   'budget_max': self.parameters.price_max,
                   'superficie_min': '',
                   'superficie_max': '',
                   'chambre_min': ''}
        response = requests.get(url=self.url, headers=self.headers, params=payload)
        soup = BeautifulSoup(response.text)

        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^(http://www\.basilic-immo\.fr/vente-{p.type}.*)(html)$".format(p=self.parameters))}):
            links.append(link.get('href'))
        return set(links)
