import pandas as pd
import re

df = pd.read_csv('raw_ingredients.csv')

df_temp = df[df['link']==df.loc[0,'link']]

df_units = pd.read_csv('units.csv')

df_ing = pd.DataFrame()

for i in df_temp['ingredient']:

	if 'span' not in i:
		variation=''
		I=i
		if ',' in i:
			I=i.split(',')[0]
			variation = i.split(',')[1]


		for u in df_units['units']:
			if u in I:
				amount = u.split('')[0].strip()


		print variation
		#print re.compile('\w+').findall(I)
		print I.split()
	




