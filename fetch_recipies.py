import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time

df_rec_links = pd.read_csv('recipe_links.csv')

base_html = 'http://allrecipes.com'

#df = pd.read_csv('raw_ingredients.csv')
df_star = pd.read_csv('ingredient_stars.csv')

#df_star = pd.DataFrame()
#df = pd.DataFrame()

q=len(df_star)+1
print q
link_set = list(set(df_rec_links['link']))

for ix in np.arange(0,2569):
	print ix


	link = link_set[ix]
	if 'video' not in link:
		#link = '/recipe/9827/chocolate-chocolate-chip-cookies-i/'
		
		html = base_html + link
		print html

		r = requests.get(html)

		#df_star = pd.DataFrame()
		soup = BeautifulSoup(r.content,'html.parser')

		'''
		results = soup.find_all('li','checkList__line')

		#df=pd.DataFrame()

		
		for r in results:
			content = r.span.contents[0]
			if 'Add all' not in content and '<span' not in content:
				try:
					content=str(content)
				except:
					content=content.encode('ascii','backslashreplace')

				if 'span' not in content:
					
					df.loc[q,'ingredient']=content
					df.loc[q,'link']=link
					q=q+1

		'''
		#df.to_csv('raw_ingredients.csv')

		#results = soup.find_all('div','rating-stars')

		#if len(results)>0:

		#df_star.loc[link,'rating']=results[0]['data-ratingstars']

		#if link not in df_star.index:
		results = soup.find_all('span','review-count')

		if len(results)>0:
			print results[0].contents
			df_star.loc[link,'ratings']=results[0].contents[0].split()[0]
			
		results = soup.find_all('div','recipe-summary__stars')
	
		if len(results)>0:
			print results[0].div['data-ratingstars']
			df_star.loc[link,'stars']=results[0].div['data-ratingstars']

		df_star.to_csv('ingredient_stars.csv')
		time.sleep(np.random.random())


