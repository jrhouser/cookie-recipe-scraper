import pandas as pd
import numpy as np
import pylab as plt
import scipy.cluster.hierarchy as sch
plt.style.use('ggplot')



def prep_data_for_clustering():
	df = pd.read_csv('parsed_ingredients.csv')



	unique,count = np.unique(df['ingredient'],return_counts=True)

	df_u=pd.DataFrame()
	df_u['unique']=list(unique)
	df_u['count']=list(count)


	df_u = df_u.sort('count',ascending=False)

	df_u = df_u[df_u['count']>200] #only keep those ingredients that appear in over 200 recipies

	print len(df_u)

	df = pd.merge(df,df_u,left_on='ingredient',right_on='unique',how='inner')


	print 'normalize'
	df['norm mL']=df['total mL']
	for u in list(set(df['link'])):

		index = df[df['link']==u].index

		for ix in index:
			df.loc[ix,'norm mL']=df.loc[ix,'total mL']/float(sum(df.loc[index,'total mL']))
		#df[df['link']==u]['total mL']=list(df[df['link']==u]['total mL']/sum(df[df['link']==u]['total mL']))


	df= df[['link','ingredient','norm mL']]

	df.to_csv('normed_ingredients.csv')


	normed_ingredients = pd.DataFrame()

	for l in list(set(df['link'])):

		#gross
		df_temp = df[df['link']==l]
		df_temp = df_temp[~df_temp['ingredient'].duplicated(keep='first')]

		for u in list(df_u['unique'].values):
			

			if u in list(df_temp['ingredient']):
				normed_ingredients.loc[str(l),str(u)]=df_temp[df_temp['ingredient']==u]['norm mL'].values[0]


	normed_ingredients.to_csv('normed_ingredients_reshape.csv')

def figure2():
	normed_ing = pd.read_csv('normed_ingredients_reshape.csv').set_index('Unnamed: 0').fillna(0)


	## some recipes have subtitued different types of flour (such as whole wheat) or butter or use egg whites only or margerin. 
	#Ignore these cases for now.
	normed_ing= normed_ing[normed_ing['all-purpose flour']>0]
	normed_ing= normed_ing[normed_ing['egg']>0]
	normed_ing = normed_ing[normed_ing['butter']>0]


	links = pd.read_csv('recipe_links.csv')
	category = pd.read_csv('category_list.csv')

	MC = list(set(category['master category']))

	links=links[links['category'].isin(MC)]

	nI = pd.merge(normed_ing,links,left_index=True,right_on='link',how='left')
	category = nI['category']
	nI=nI[[c for c in normed_ing.columns]]



	df_av=pd.DataFrame(columns=nI.columns)
	for m in MC:
		
		df_av.ix[m]=np.mean(nI.ix[category==m]) 

	print max(df_av)

	df_av=df_av.fillna(0)
	df_av = df_av.drop('Cookie Icing and Frosting')  # this class isn't really a cookie. so remove it.
	linkage_matrix = sch.linkage(df_av.values)
	df_av=np.log10(df_av)


	plt.figure(figsize = (15,6))
	plt.subplot(121)
	Z=sch.dendrogram(linkage_matrix,
	           labels=list(df_av.index),orientation='left')

	plt.tight_layout()
	ax=plt.subplot(122)
	D=df_av.values[Z['leaves'],:]
	im = ax.matshow(D,aspect='auto',origin='lower')
	plt.xticks(np.arange(len(df_av.columns)),df_av.columns,rotation='vertical')
	#ax.set_xticks([])
	ax.set_yticks([])
	plt.colorbar(im)
	plt.savefig('figure2b.pdf')

	plt.show()


prep_data_for_clustering()
figure2()



