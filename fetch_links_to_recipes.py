import pandas as pd
from bs4 import BeautifulSoup
import requests


df_cat=pd.read_csv('./category_list.csv')

base_html='http://allrecipes.com'

html = base_html+df_cat['master links'].ix[0]

r= requests.get(html)

c=r.content



soup = BeautifulSoup(c,'html.parser')

results = soup.find_all('article','grid-col--fixed-tiles')


print results[0].a["href"]
print results[0].img["title"]


