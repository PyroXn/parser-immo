import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class OptimHome(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.OPTIMHOME_URL+'catalog/advanced_search_result.php')
        self.parameters = parameters

    def get_links(self):
        payload = {'action': 'update_search',
                   'map_polygone': '',
                   'C_28_search': 'EGAL',
                   'C_28_type': 'UNIQUE',
                   'C_28': 'Vente',
                   'C_27_search': 'EGAL',
                   'C_27_type': 'UNIQUE',
                   'C_27': '10,24',
                   'C_30_MIN_small': 0,
                   'C_30_MAX_small': '',
                   'C_34_MIN_small': 0,
                   'C_34_MAX_small': '',
                   'C_65_search': 'CONTIENT',
                   'C_65_type': 'TEXT',
                   'C_65_old': 'TEXT',
                   'C_65_temp': '',
                   'C_30_search': 'COMPRIS',
                   'C_30_type': 'NUMBER',
                   'C_30_MIN': 0,
                   'C_30_MAX': self.parameters.price_max,
                   'C_34_search': 'COMPRIS',
                   'C_34_type': 'NUMBER',
                   'C_34_MIN': self.parameters.surface_min,
                   'C_34_MAX': '',
                   'C_1831_search': 'EGAL',
                   'C_1831_type': 'UNIQUE',
                   'C_1831': '',
                   'C_1831_temp': '',
                   'C_33_search': 'SUPERIEUR',
                   'C_33_type': 'NUMBER',
                   'C_33_MIN': '',
                   'C_38_search': 'SUPERIEUR',
                   'C_38_type': 'NUMBER',
                   'C_38_MIN': '',
                   'C_36_search': 'COMPRIS',
                   'C_36_type': 'NUMBER',
                   'C_36_MIN': '',
                   'C_36_MAX': '',
                   'keywords': '',
                   'C_124_search': 'EGAL',
                   'C_124_type': 'UNIQUE',
                   'C_211_search': 'EGAL',
                   'C_211_type': 'UNIQUE',
                   'C_65': '54400 LONGWY',
                   'C_64_search': 'INFERIEUR',
                   'C_64_type': 'TEXT',
                   'C_64': self.parameters.radius}
        response = requests.get(url=self.url, headers=self.headers, params=payload)
        soup = BeautifulSoup(response.text)

        links = []
        for link in soup.findAll('a', attrs={'class': 'list_titre_bien', 'href': re.compile("^\.\./fiches")}):
            links.append(url.OPTIMHOME_URL + link.get('href')[3:])
        return set(links)
