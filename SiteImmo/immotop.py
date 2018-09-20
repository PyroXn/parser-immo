import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class Immotop(SiteImmo):
    def __init__(self, parameters):
        SiteImmo.__init__(self, url.IMMOTOP_URL)
        self.parameters = parameters

    def get_links(self):
        payload = {'form': 'quick_search_sale',
                   'f[from]': 13,
                   'f[tender]': 0,
                   'f[Type]': 'sale',
                   'f[radius]': self.parameters.radius,
                   'f[cat_mode]': '',
                   'f[top_category]': 'home',
                   'f[country]': 'france',
                   'f[Parent_ID]': 400,
                   'f[city]': self.parameters.city,
                   'cat_mode': 'on',
                   'f[rooms][from]': '',
                   'f[surface][from]': self.parameters.surface_min,
                   'f[price][from]': '',
                   'f[price][to]': self.parameters.price_max}
        response = requests.post(url=self.url, headers=self.headers, data=payload)
        soup = BeautifulSoup(response.text)
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^(https://www\.immotop\.lu/properties/used/ground/.*)(?<!contact)$")}):
            links.append(link.get('href'))
        return set(links)
