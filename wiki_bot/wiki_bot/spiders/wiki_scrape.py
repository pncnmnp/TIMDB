import scrapy
import json
from bs4 import BeautifulSoup

class WikiScrape(scrapy.Spider):
	name = "wikibot"
	def __init__(self):
		pass

	def start_requests(self):
		urls = json.load(open(".././wiki_dump/wiki_titles_2010-2019.json"))
		for url in urls:
			yield scrapy.Request(url=('https://en.wikipedia.org' + url), callback=self.parse)

	def parse(self, response):
		soup = BeautifulSoup(response.text, 'html5lib')
		imdb_id = str()
		poster_path = str()
		title = soup.findAll("h1")[0].text
		wiki_title = response.request.url

		for link in soup.findAll("a"):
			try:
				if 'imdb.com' in link.get('href'):
					imdb_id = link.get('href')
			except:
				pass

		try:
			poster_path = "https://" + soup.findAll("img", class_="thumbborder")[0].get("src")
		except:
			pass

		with open("../bollywood.csv", 'a') as f:
			f.write(title + "," + imdb_id.replace("https://www.imdb.com/title/", "").replace("/", "") + "," + poster_path + "," + wiki_title + "\n")
		self.log("saved wiki title %s" % wiki_title)