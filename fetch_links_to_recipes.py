import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import numpy as np

base_html='http://allrecipes.com'


def fetch_links(cat,header,df_rec_links,q):
	for m in cat:
		cat= np.unique(df_cat[df_cat[header+'links']==m][header+'category'])
		for page in range(50):
			print m + ' page='+str(page)
			html = base_html+m+'/?page='+str(page)

			r= requests.get(html)

			c=r.content


			soup = BeautifulSoup(c,'html.parser')

			results = soup.find_all('section','error_page')
			if len(results)>0:
				break
			
			results = soup.find_all('article','grid-col--fixed-tiles')



			for r in results:
				if type(r.a)!=type(None) and r.img.has_attr('title'):
		 				if r.a["href"] not in list(df_rec_links['link']):
							df_rec_links.loc[q,'link']=r.a["href"]
							df_rec_links.loc[q,'title']=r.img["title"]
							df_rec_links.loc[q,'category']=master_cat
							q=q+1
						
							
			time.sleep(np.random.random()*10)


		df_rec_links.to_csv('recipe_links.csv')

		return df_rec_links

df_cat=pd.read_csv('./category_list.csv')

df_rec_links = pd.DataFrame(columns=['link','title','category'])

master_cat = np.unique(df_cat['master links'])

cat = np.unique(df_cat['category'])

df_rec_links=fetch_links(master_cat,'master ',df_rec_links,0)
df_rec_links=fetch_links(cat,'',df_rec_links,len(df_rec_links))




