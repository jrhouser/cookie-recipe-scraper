import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time

BASE_HTML= 'http://allrecipes.com'

#df = pd.read_csv('raw_ingredients.csv')
#df_star = pd.read_csv('ingredient_stars.csv')


def fetch(fileout,rawfileout,rec_link_file):
	

	df_rec_links = pd.read_csv(rec_link_file)

	df_star = pd.DataFrame()
	df = pd.DataFrame()

	q=len(df_star)+1
	print q
	link_set = list(set(df_rec_links['link']))

	for ix in np.arange(0,len(link_set)):
		print ix


		link = link_set[ix]
		if 'video' not in link:
			
			html = BASE_HTML + link

			r = requests.get(html)

			soup = BeautifulSoup(r.content,'html.parser')

		
			results = soup.find_all('li','checkList__line')

			
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

			df.to_csv(rawfileout)

			
			results = soup.find_all('span','review-count')

			if len(results)>0:
				print results[0].contents
				df_star.loc[link,'ratings']=results[0].contents[0].split()[0]
				
			results = soup.find_all('div','recipe-summary__stars')
		
			if len(results)>0:
				print results[0].div['data-ratingstars']
				df_star.loc[link,'stars']=results[0].div['data-ratingstars']

			df_star.to_csv(fileout)
			time.sleep(np.random.random())


if __name__ == "__main__":
	rec_link_file = 'recipe_links.csv'
	rawfileout = 'raw_ingredients.csv'
	fileout = 'ingredient_stars.csv'

	fetch(fileout,rawfileout,rec_link_file)


