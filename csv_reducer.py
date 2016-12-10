import os

def main(file_list, stoping_point):
	"""Read lines from csv file and write to new file"""
	for file in file_list:

		with open('data/'+file[:-4]+'_mini.csv', 'w') as outfile, open('data/'+file, 'r') as infile:

			line_count = 0
			for line in infile:
				if line_count == stoping_point:
					break
				else:
					outfile.write(line)
					line_count += 1



def file_mover(file_list):

	for file in file_list:
	
		source = 'data/'+file[:-4]+'_mini.csv'
		destination = 'data_mini/'+file[:-4]+'_mini.csv'
		os.rename(source, destination)
	return




row_number = 50000
file_names = ['documents_categories.csv',
			  'clicks_test.csv',
			  'documents_meta.csv',
			  'documents_entities.csv',
			  'promoted_content.csv',
			  'sample_submission.csv',
			  'documents_topics.csv',
			  'clicks_train.csv',
			  'events.csv',
			  'page_views_sample.csv']

main(file_names, row_number)
file_mover(file_names)

