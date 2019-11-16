from PATHS import *
import pandas as pd
import json

def get_crew_ids():
	 return json.load(open(crew_ids_path))

def get_title():
	df = pd.read_csv(name_path, sep='\t', chunksize=200000, low_memory=False, encoding="ISO-8859-1")
	return df

def map_titles():
	ids = sorted(get_crew_ids())
	cntr = 0

	for df_iter in pd.read_csv(name_path, sep='\t', chunksize=200000, low_memory=False):
		df_ids = df_iter['nconst'].tolist()

		for crew_id in ids:
			if crew_id in df_ids:
				df_val = df_iter[df_iter['nconst'] == crew_id]
				with open("./bollywood_crew_data.csv", 'a') as f:
					print("FETCHING: " + str(crew_id) + " DONE: " + str(cntr))
					f.write(str(crew_id) + "," + str(df_val.values[0][1]) + "," + str(df_val.values[0][2]) + "," + str(df_val.values[0][3]) + "," + str(df_val.values[0][4]).replace(",","|") + "," + str(df_val.values[0][5]).replace(",", "|") + "\n")
					f.close()
					cntr = cntr + 1

if __name__ == '__main__':
	map_titles()