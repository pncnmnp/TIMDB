from PATHS import *
import pandas as pd
import json

def get_imdb_ids():
	 return json.load(open(movielens_match_imdb))

def get_ratings():
	df = pd.read_csv(movie_lens_links_path, chunksize=200000, low_memory=False, encoding="ISO-8859-1")
	return df

def map_ids():
	ids = sorted(get_imdb_ids())
	cntr = 0

	for df_iter in pd.read_csv(movie_lens_links_path, chunksize=200000, low_memory=False):
		df_ids = df_iter['imdbId'].tolist()

		for movie_id in ids:
			if movie_id in df_ids:
				df_val = df_iter[df_iter['imdbId'] == movie_id]
				with open("./movielens_links.csv", 'a') as f:
					print("FETCHING: " + str(movie_id) + " DONE: " + str(cntr))
					f.write(str(int(df_val.values[0][0])) + "," + str(int(df_val.values[0][1])) + "\n")
					f.close()
					cntr = cntr + 1

if __name__ == '__main__':
	map_ids()