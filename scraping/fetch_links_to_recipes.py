import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import numpy as np

BASE_HTML='http://allrecipes.com'

def fetch_links(category,header,df_rec_links,q,outputfile):

	for m in category:
		
			cat = np.unique(df_cat[df_cat[header+'links']==m][header+'category'].values)
			for page in np.arange(0,100):
				print m + ' page='+str(page)
				html = BASE_HTML+m+'/?page='+str(page)

				r = requests.get(html)

				c = r.content

				soup = BeautifulSoup(c,'html.parser')

				results = soup.find_all('section','error-page')
				if len(results)>0:
					break
				
				results = soup.find_all('article','grid-col--fixed-tiles')

				for r in results:
					if type(r.a)!=type(None) and r.img.has_attr('title'):
			 				if r.a["href"] not in list(df_rec_links['link']):
								df_rec_links.loc[q,'link']=r.a["href"]
								df_rec_links.loc[q,'title']=r.img["title"].encode('ascii','backslashreplace')
								df_rec_links.loc[q,'category']=cat[0]
								
							else:
								index=df_rec_links[df_rec_links['link']==r.a["href"]].index[0]
								if df_rec_links.loc[index,'category']!=str(cat[0]):
									df_rec_links.loc[q,'link']=r.a["href"]
									df_rec_links.loc[q,'title']=r.img["title"].encode('ascii','backslashreplace')
									df_rec_links.loc[q,'category']=cat[0]
								

							
							q=q+1
					df_rec_links.to_csv(outputfile)	

				time.sleep(np.random.random()*5)


	return df_rec_links


def fetch(category_filename,outputfile):
	df_cat=pd.read_csv('./category_list.csv')
	df_rec_links = pd.DataFrame(columns=['link','title','category'])
	#df_rec_links = pd.read_csv('recipe_links.csv').set_index('Unnamed: 0')

	master_cat = np.unique(df_cat['master links'])
	master_cat = master_cat
	cat = np.unique(df_cat['links'])

	df_rec_links=fetch_links(master_cat,'master ',df_rec_links,len(df_rec_links)+1,outputfile)
	df_rec_links=fetch_links(cat,'',df_rec_links,len(df_rec_links)+1,outputfile)


if __name__=="__main__":

	outputfile='recipe_links.csv'
	category_filename='category_list.csv'

	fetch(category_filename,outpufile)





