from bs4 import BeautifulSoup
import requests
import pandas as pd

html='http://allrecipes.com/recipes/362/desserts/cookies/'


def types(html):
	
	r=requests.get(html)

	html_doc=r.content

	soup = BeautifulSoup(html_doc,'html.parser')
	
	cat=[]
	cat_links=[]
	S=soup.find_all('div','hub-daughters__container')
	if len(S)>0:
		for types in S[0].find_all('img',''):
			cat.append(types['title'])
		

		cat_links=[]
		for types in S[0].find_all('a'):
			cat_links.append(types['href'])
	return cat_links,cat




cat_links,cat=types(html)

df_cat = pd.DataFrame()

master_cat,master_links,sub_cat_links,sub_cat=[],[],[],[]

for i,c in enumerate(cat_links):

	sub_cat_links_t,sub_cat_t=types('http://allrecipes.com'+c)
	#print sub_cat_links_t+sub_cat_links
	sub_cat_links_t=[str(x) for x in sub_cat_links_t]
	sub_cat_t=[str(x) for x in sub_cat_t]
	sub_cat_links=sub_cat_links+sub_cat_links_t
	sub_cat=sub_cat+sub_cat_t

	master_cat=master_cat+[str(cat[i])]*len(sub_cat_t)	
	master_links=master_links+[str(cat_links[i])]*len(sub_cat_t)



df_cat['category'] = sub_cat
df_cat['links'] = sub_cat_links
df_cat['master category'] = master_cat
df_cat['master links'] = master_links

df_cat.to_csv('./category_list.csv')




