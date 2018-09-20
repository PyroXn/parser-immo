import re

import requests
from BeautifulSoup import BeautifulSoup

import url
from siteimmo import SiteImmo


class ReMax(SiteImmo):
    def __init__(self):
        SiteImmo.__init__(self, url.REMAX_URL)

    def get_links(self):
        payload = {'mode': 'GalleryView',
                   'tt': 261,
                   'cr': 2,
                   'r': 280,
                   'p': 2767,
                   'pt': 2901,
                   'max': 200000,
                   'cur': 'EUR',
                   'la': 'All',
                   'sb': 'PriceDecreasing',
                   'page': 1,
                   'sc': 65,
                   'sid': '1574c058-0111-45c7-889e-87e9fed7431f'}
        param = 'PublicListingList.aspx#mode=GalleryView&tt=261&cr=2&r=280&p=2767&pt=2901&max=200000&cur=EUR&la=All&sb=PriceDecreasing&page=1&sc=65&sid=1574c058-0111-45c7-889e-87e9fed7431f'
        response = requests.get(url='http://www.remax.lu/PublicListingList.aspx?SelectedCountryID=65',
                                headers=self.headers, params=payload)
        print response.text
        print response.url
        soup = BeautifulSoup(response.text)

        links = []
        for link in soup.findAll('a', attrs={'class': 'LinkImage'}):
            links.append(link.get('href'))
        return set(links)
