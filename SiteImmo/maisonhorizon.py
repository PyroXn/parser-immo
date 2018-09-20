import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class MaisonHorizon(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.MAISONSHORIZON_URL)
        self.parameters = parameters

    def get_links(self):
        param = 'annonces/terrains-vendre/longwy-54400.aspx?rad={p.radius}&px=mx%3a{p.price_max}&sft=mn%3a{p.surface_min}&rm=1'.format(p=self.parameters)
        response = requests.get(url=self.url+param, headers=self.headers)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^/annonce/terrain-vendre/")}):
            links.append(self.url + link.get('href'))
        return set(links)
