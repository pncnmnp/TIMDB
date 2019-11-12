from PATHS import *
import pandas as pd
import json

def get_imdb_ids():
	 return json.load(open(imdb_ids_path))

def get_title():
	df = pd.read_csv(title_path, sep='\t', chunksize=200000, low_memory=False, encoding="ISO-8859-1")
	return df

def map_titles():
	ids = sorted(get_imdb_ids())
	cntr = 0

	for df_iter in pd.read_csv(title_path, sep='\t', chunksize=200000, low_memory=False):
		df_ids = df_iter['tconst'].tolist()

		for imdb_id in ids:
			if imdb_id in df_ids:
				df_val = df_iter[df_iter['tconst'] == imdb_id]
				with open("./bollywood_meta.csv", 'a') as f:
					print("FETCHING: " + str(imdb_id) + " DONE: " + str(cntr))
					f.write(str(imdb_id) + "," + str(df_val.values[0][2]) + "," + str(df_val.values[0][3]) + "," + str(df_val.values[0][4]) + "," + str(df_val.values[0][5]) + "," + str(df_val.values[0][7]) + "," + str(df_val.values[0][8]).replace(",", "|") + "\n")
					f.close()
					cntr = cntr + 1

if __name__ == '__main__':
	map_titles()