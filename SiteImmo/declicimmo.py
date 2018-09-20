import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class DeclicImmo(SiteImmo):
    def __init__(self):
        SiteImmo.__init__(self, url.DECLICIMMO_URL)

    def get_links(self):
        param = '001_resultat.php?venteloc=1&typebien=terrain&ville=Toutes&Submit=Voir'
        response = requests.get(url=self.url+param, headers=self.headers)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^002_detail.php")}):
            links.append(self.url + link.get('href'))
        return set(links)
