#!/usr/bin/python
from collections import namedtuple
import sys
from SiteImmo.basilic import Basilic
import pandas as pd

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

Parameters = namedtuple('Parameters', ['type', 'city', 'radius', 'surface_min', 'price_max'])
param = Parameters('maison', 'Longwy', 15, 700, 150000)
articles = []
basilic = Basilic(param)
basilic.start()
basilic.join()

for article in basilic.articles:
    print(article.final_url)
    articles.append({'url': article.final_url, 'title': article.title, 'meta_description': article.meta_description,
                     'text': article.cleaned_text})

df = pd.DataFrame(articles)
df = df[['url', 'title', 'meta_description', 'text']]

print(df)