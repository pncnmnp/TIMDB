from PATHS import *
import pandas as pd
import json

def get_imdb_ids():
	 return json.load(open(imdb_ids_path))

def get_ratings():
	df = pd.read_csv('ratings.tsv', sep='\t', header=0)
	return df

def map_ratings():
	ids = get_imdb_ids()
	df = get_ratings()
	df_ids = df['tconst'].tolist()
	cntr = 0

	for imdb_id in ids:
		if imdb_id in df_ids:
			df_val = df[df['tconst'] == imdb_id]
			with open("./bollywood_ratings.csv", 'a') as f:
				print("FETCHING: " + str(imdb_id) + " DONE: " + str(cntr))
				f.write(str(imdb_id) + "," + str(df_val.values[0][1]) + "," + str(df_val.values[0][2]) + "\n")
				f.close()
		# else:
		# 	print(imdb_id)

			cntr = cntr + 1

if __name__ == '__main__':
	map_ratings()	