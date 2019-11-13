import scrapy
import json
from bs4 import BeautifulSoup

class ImdbScrape(scrapy.Spider):
	name = "imdbbot"
	def __init__(self):
		pass

	def start_requests(self):
		urls = json.load(open(".././wiki_dump/imdb_ids_1990-2009.json"))
		for url in urls:
			yield scrapy.Request(url=('https://www.imdb.com/title/' + url), callback=self.parse)

	def parse(self, response):
		bs = BeautifulSoup(response.text, 'html5lib')
		imdb_url = response.request.url
		imdb_id = imdb_url.replace("https://www.imdb.com/title/", "").replace("/", "")
		wins_nominations = str()
		story = str()
		summary = str()
		actors = str()
		tagline = str()

		try:
			wins_nominations = bs.findAll("span", class_="awards-blurb")[0].text.replace(".", "").strip()
		except:
			pass

		try:
			release_date = bs.findAll("div", class_="subtext")[0].text.strip().split("|")[3].strip()
		except:
			try:
				release_date = bs.findAll("div", class_="subtext")[0].text.strip().split("|")[2].strip()
			except:
				release_date = str()

		try:
			summary = bs.findAll("div", class_="summary_text")[0].text.strip()
		except:
			pass

		try:
			for i in range(1, len(bs.findAll("table", class_="cast_list")[0].findAll("tr"))-1):
				actors = actors + bs.findAll("table", class_="cast_list")[0].findAll("tr")[i].findAll("td")[1].text.strip() + "|"
		except:
			pass

		try:
			story = bs.findAll("div", id="titleStoryLine")[0].findAll("div", class_="inline canwrap")[0].findAll("span")[0].text.strip()
		except:
			pass

		try:
			if bs.findAll("div", class_="txt-block")[0].findAll("h4")[0].text == "Taglines:":
				tagline = bs.findAll("div", class_="txt-block")[0].text.replace("Taglines:", "").strip()
		except:
			pass

		with open("../bollywood_text.csv", 'a') as f:
			f.write(imdb_id + "," + story.replace(",", " ").replace("\n", "") + "," + summary.replace(",", " ").replace("See full summary »", "").replace("See more »", "").replace("\n", "") + "," + tagline.replace(",","|").replace("\n", "") + "," + actors.replace("\n", "") + "," + wins_nominations.replace("\n", "") + "," + release_date.replace("\n", "") + "\n")
		self.log("saved imdb data for %s" % imdb_url)