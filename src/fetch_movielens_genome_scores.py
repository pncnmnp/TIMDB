from PATHS import *
import pandas as pd
import json

def get_movie_ids():
	 return json.load(open(movielens_match_movieid))

def get_ratings():
	df = pd.read_csv(movie_lens_genome_scores_path, chunksize=200000, low_memory=False, encoding="ISO-8859-1")
	return df

def map_titles():
	ids = sorted(get_movie_ids())
	cntr = 0

	for df_iter in pd.read_csv(movie_lens_genome_scores_path, chunksize=200000, low_memory=False):
		df_ids = df_iter['movieId'].tolist()

		for movie_id in ids:
			if movie_id in df_ids:
				df_val = df_iter[df_iter['movieId'] == movie_id]
				with open("./movielens_genome_scores.csv", 'a') as f:
					print("FETCHING: " + str(movie_id) + " DONE: " + str(cntr))
					for tag_id in range(0, len(df_val)):
						f.write(str(int(df_val.values[tag_id][0])) + "," + str(int(df_val.values[tag_id][1])) + "," +str(df_val.values[tag_id][2]) + "\n")
					f.close()
					cntr = cntr + 1

if __name__ == '__main__':
	map_titles()