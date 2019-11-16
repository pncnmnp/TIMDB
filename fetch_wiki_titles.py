from PATHS import *
import requests
from bs4 import BeautifulSoup
import json

def open_wiki_titles():
	wiki_title_list = json.load(open(wiki_titles))
	return wiki_title_list

def store_wiki_titles(data):
	with open(wiki_titles, 'w') as f:
		json.dump(data, f)

def get_wiki_titles():
	html = requests.get('https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_1950')
	bs = BeautifulSoup(html.text, 'html5lib')
	wiki_title_list = open_wiki_titles()

	# THE RANGE HAS TO BE CHANGED MANUALLY FOR EACH WIKI URL
	# AS THE FORMATTING IS NOT CONSISTENT
	for section in range(0, 4):
		quarter_sect = bs.find_all("table", class_="wikitable")[section]
		total_quarter_movies = len(quarter_sect.findAll("tr"))

		for film_no in range(1, total_quarter_movies):
			try:
				check_1 = len(quarter_sect.findAll("tr")[film_no].findAll("td")[0].findAll("a"))
			except:
				check_1 = 0
			try:
				check_2 = len(quarter_sect.findAll("tr")[film_no].findAll("td")[1].findAll("a"))
			except:
				check_2 = 0

			if check_1 == 1 or check_2 == 1:
				wiki_link = quarter_sect.findAll("tr")[film_no].findAll("a")[0].get("href")
				if wiki_link in wiki_title_list or '/w/' in wiki_link:
					continue
				wiki_title_list.append(wiki_link)
				print("Added: " + str(wiki_link))

	store_wiki_titles(wiki_title_list)

if __name__ == '__main__':
	get_wiki_titles()