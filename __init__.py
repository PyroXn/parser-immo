from collections import namedtuple

import pandas as pd
import pygsheets as pg

from SiteImmo.basilic import Basilic
from SiteImmo.capifrance import CapiFrance
from SiteImmo.immotop import Immotop
from SiteImmo.maisonhorizon import MaisonHorizon
from SiteImmo.optimhome import OptimHome
from SiteImmo.rthill import RThill
from SiteImmo.safti import Safti

gc = pg.authorize(
    outh_file='client_secret_290983420794-u4mdodpe6a0u84sd424ol5v20873me96.apps.googleusercontent.com.json')
sh = gc.open_by_key('11nWf5fixg_9XAS6-tuYPWJpPYi1bMymYOC5-gBTyrKA')
wks = sh.sheet1

# WORK
Parameters = namedtuple('Parameters', ['type', 'city', 'radius', 'surface_min', 'price_max'])

param = Parameters('terrain', 'Longwy', 15, 700, 150000)
articles = []
sites = [Immotop(param), Safti(param), OptimHome(param), MaisonHorizon(param), CapiFrance(param), RThill(param),
         Basilic(param)]
map(lambda site: site.start(), sites)
for site in sites:
    site.join()
    for article in site.articles:
        articles.append({'url': article.final_url, 'title': article.title, 'meta_description': article.meta_description,
                         'text': article.cleaned_text})

df = pd.DataFrame(articles)
df = df[['url', 'title', 'meta_description', 'text']]
wks.set_dataframe(df=df, start='A1')
# print df
# print(df[0].to_json(orient='records'))
# print(tabulate(df, headers='keys', tablefmt='psql'))

# FIXME localite + parse article
# Panetta().get_articles()

# FAIL
# DeclicImmo().get_articles()
# ReMax().get_articles()
