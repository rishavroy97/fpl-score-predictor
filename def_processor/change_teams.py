import numpy as np
import pandas as pd

df = pd.read_csv('../def_result_files/def_data.csv')

rank5=['MCI']
rank4=['ARS','CHE','EVE','LIV','MUN','TOT']
rank3=['BUR','CRY','LEI','NEW','SOU','STK','SWA','WHU']


for i in range(0,len(df)) :
	if df.loc[i, 'team'] in rank5 :
		df.loc[i, 'team']=5

	elif df.loc[i, 'team'] in rank4 :
		df.loc[i, 'team']=4

	elif df.loc[i, 'team'] in rank3 :
		df.loc[i, 'team']=3

	else :
		df.loc[i, 'team']=2


for i in range(0,len(df)) :
	if df.loc[i, 'opponent'] in rank5 :
		df.loc[i, 'opponent']=5

	elif df.loc[i, 'opponent'] in rank4 :
		df.loc[i, 'opponent']=4

	elif df.loc[i, 'opponent'] in rank3 :
		df.loc[i, 'opponent']=3

	else :
		df.loc[i, 'opponent']=2

df.to_csv('../def_result_files/def_data.csv',index=False)