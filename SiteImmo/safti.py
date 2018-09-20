import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class Safti(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.SAFTI_URL)
        self.parameters = parameters

    def get_links(self):
        param = 'acheter/{p.type}/longwy-54400/budgetmax-{p.price_max}/distance-{p.radius}/terrainMini-{p.surface_min}'.format(p=self.parameters)
        response = requests.get(url=self.url + param, headers=self.headers)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http://www\.safti\.fr/annonces/achat/terrain/.*")}):
            links.append(link.get('href'))
        return set(links)
