import pandas as pd
import pylab as plt
import numpy as np
import scipy.cluster.hierarchy as sch
plt.style.use('ggplot')

def figure1():


	links = pd.read_csv('recipe_links.csv')

	stars = pd.read_csv('ingredient_stars.csv').fillna(0)

	stars = stars.set_index('Unnamed: 0')
	merged = pd.merge(links,stars,left_on='link',right_index=True,how='inner')
	merged=merged.fillna(0)

	category = pd.read_csv('category_list.csv')

	mast_cat = list(set(category['master category']))
	df_pop = pd.DataFrame()

	for m in mast_cat:

		M=merged[merged['category']==m]
		C=category[category['master category']==m]['category']
		for c in C: 
			M=pd.concat([M,merged[merged['category']==c]],axis=0)


		M=M[~M['link'].duplicated(keep='first')]
		
		df_pop.loc[m,'average reviews']=np.mean(M['ratings'])#(np.mean(M['rating'])-np.mean(merged['rating']))/np.std(merged['rating'])
		df_pop.loc[m,'5 stars'] = np.sum(M['stars']>=4.5)/float(len(M['stars']))#-np.mean(merged['stars']))/np.std(merged['stars'])
		df_pop.loc[m,'total recipies'] = len(M)


	fig, ax = plt.subplots(figsize=(20,10))
	ax.bar(np.arange(len(mast_cat))-0.25,df_pop['average reviews']/max(df_pop['average reviews']),width=0.2)
	ax.bar(np.arange(len(mast_cat)),df_pop['5 stars']/max(df_pop['5 stars']),color='red',width=0.2)
	ax.bar(np.arange(len(mast_cat))+0.25,df_pop['total recipies']/max(df_pop['total recipies']),color='c',width=0.2)

	ax.set_xticks(np.arange(len(mast_cat)))
	ax.set_xticklabels(mast_cat,rotation='vertical')
	ax.legend(['average reviews','fraction with over 4.5 stars','total recipies in category'],loc=0)
	plt.ylabel('normalized value')
	plt.xlabel('category')
	plt.tight_layout()
	plt.show()

figure1()





