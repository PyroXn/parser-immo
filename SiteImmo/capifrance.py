import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class CapiFrance(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.CAPIFRANCE_URL + 'search/run')
        self.parameters = parameters

    def get_links(self):
        payload = {'capi_search[sort]': '',
                   'capi_search[distance]': '10km',
                   'capi_search[searchType]': 1,
                   'capi_search[query]': '',
                   'capi_search[propertyType][]': 3,
                   'capi_search[budget][min]': 0,
                   'capi_search[budget][max]': self.parameters.price_max,
                   'capi_search[area][min]': self.parameters.surface_min,
                   'capi_search[area][max]': 0,
                   'capi_search[selected]': 'city_59269:LONGWY(54400):49.514528500025|5.769264099994'}
        response = requests.post(url=self.url, headers=self.headers, data=payload)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http://www\.capifrance\.fr/annonces/achat/terrain-constructible/montigny-sur-chiers/340939202510")}):
            links.append(link.get('href'))
        return set(links)
