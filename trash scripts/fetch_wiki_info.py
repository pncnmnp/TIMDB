from bs4 import BeautifulSoup
import json
import pandas as pd
import wptools
from PATHS import *
import fetch_wiki_titles

def get_imdb_id(bs):
	for temp in bs.findAll('template'):
		try:
			if 'imdb' in temp.find('title').text.lower():
				return temp.find('value').text
		except:
			return None

def update_csv(df):
	with open(db_csv, 'w') as f:
		df.to_csv(f, header=f.tell()==0)

def get_wiki_info():
	links = fetch_wiki_titles.open_wiki_titles()
	df = pd.read_csv(db_csv)
	cntr = 0

	# try:
	for link in links:
		link_mod = link.replace('/wiki/', '')

		if 'https://en.wikipedia.org/wiki/' + link_mod in df['wiki_link'].tolist():
			print("ALREADY FETCHED: " + link_mod)
			continue

		print("FETCH: "+str(cntr))
		page = wptools.page(link_mod)
		try:
			film = page.get_parse()
			film_title = film.data['title']

		except:
	 		print("FAILED: " + link_mod)
	 		continue

		try:
			film_poster = film.images()[0]['url']
		except:
			film_poster = None
		try:
			film_imdb_id = get_imdb_id(BeautifulSoup(film.data['parsetree'], 'html5lib'))
			if film_imdb_id[:2] != 'tt':
				film_imdb_id = "tt" + film_imdb_id
		except:
			links.remove('/wiki/'+link_mod)
			fetch_wiki_titles.store_wiki_titles(links)
			continue

		print((film_title, film_imdb_id, film_poster))

		film_wiki_link = 'https://en.wikipedia.org/wiki/' + link_mod

		df.loc[-1] = [film_title, film_imdb_id, film_poster, film_wiki_link, '', '', '', '', '', '', '', '', '', '', '']
		df.index = df.index + 1
		print("FETCHED: " + film_title)

		cntr = cntr + 1

		if cntr == 20:
			df.sort_index(inplace=True)
			update_csv(df)
			cntr = 0
	df.sort_index(inplace=True)
	update_csv(df)
	# except:
	# 	df.sort_index(inplace=True)
	# 	update_csv(df)
	# 	print("TERMINATED!!!!! RESTART IT!")		

if __name__ == '__main__':
	get_wiki_info()