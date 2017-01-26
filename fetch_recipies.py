import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


df_rec_links = pd.read_csv('recipe_links.csv')

link = df_rec_links.loc[0,'link']

base_html = 'http://allrecipes.com'
html = base_html + link
print html

r = requests.get(html)


soup = BeautifulSoup(r.content,'html.parser')

results = soup.find_all('li','checkList__line')

for r in results:
	content = r.span.contents[0]
	if 'Add all' not in content and '<span' not in content:
		print content



