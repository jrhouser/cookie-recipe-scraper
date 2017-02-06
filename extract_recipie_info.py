import pandas as pd
import numpy as np

df_ing = pd.read_csv('raw_ingredients.csv')

links = list(set(df_ing['link']))

dfunits = pd.read_csv('units.csv').set_index('unit')

for ix in df_ing.index:
	s = df_ing.loc[ix,'ingredient']
	if 'optional' in s:
		s=s.strip('(optional)')
	


	#s=i.strip('(optional)')
	
	if len(s)>3:


		if '/'==s[3]:
			
			amount = float(s[0]) + float(s[2])/float(s[4])
			unit = s.split()[2].strip('s')
			ingredient = ' '.join(s.split()[3::]).split(',')[0]


		elif '/'==s[1]:
			amount = float(s[0])/float(s[2])
			unit = s.split()[1].strip('s')

			ingredient = ' '.join(s.split()[2::]).split(',')[0]

		elif '('==s[2]:

			
			amount = float(s[0])*float(s.split('(')[1].split('-')[0].split()[0])

			unit = s.split('(')[1].split()[1].strip(')').strip('s')
			ingredient = s.split(')')[1].lstrip(' ').split(',')[0]

		else:
			
			amount = s.split()[0]
			try:
				amount = float(amount)
			except:
				amount = 0.0

			if len(s.split())>1:
				unit = s.split()[1].strip('s')
			else:
				unit = '1'
			ingredient = ' '.join(s.split()[2::]).split(',')[0]

		if unit not in dfunits.index:
			ingredient=unit+' '+ingredient
			unit = 'object'

		if 'egg' in unit:
			ingredient='egg'

		df_ing.loc[ix,'amount'] = amount
		df_ing.loc[ix,'unit'] = unit
		df_ing.loc[ix,'ingredient'] = ingredient
		


df_ing = pd.merge(df_ing,dfunits,left_on='unit',right_index=True,how='left')
df_ing['total mL']=np.multiply(df_ing['amount'],df_ing['ml'])

df_ing.to_csv('parsed_ingredients.csv')


