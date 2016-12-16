import pandas as pd
import numpy as np
import os

global DF

def import_data(filename, dtypes, directory = 'data/'):
	global DF
	
	try:
		DF = pd.read_csv(directory + filename, dtype=dtypes) #read mini DF into memory
		print '.csv imported correctly as DataFrame.'
		print('\a')
	except:
		pass
	
	return DF


def write_data(df):
	for group_name, group_data in df.groupby('clicked'):
		filename = 'clicked_' + str(group_name) + '.csv'
		
		try:
			os.remove(filename) #delete old csv cleaned file
			print filename + ' already exists, deleting it now.'
		except:
			print filename+ ' does not exist, generating new file.'

		group_data.to_csv('data/' + filename, index=False)
		
		print '.csv file generated!'
		print('\a')


dtypes = {'display_id' : np.int32, 'ad_id': np.int32, 'clicked': np.int8}
#import_data('clicks_train_mini.csv', dtypes, directory = 'data_mini/')
import_data('clicks_train.csv', dtypes, directory = 'data/')

write_data(DF)


