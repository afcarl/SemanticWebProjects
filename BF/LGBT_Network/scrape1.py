#!usr/bin/env python2.7

"""
Scraping the links for LGBT articles on BuzzFeed
"""

import os,sys
import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import urllib
import pickle

PIK = "pickle.dat"
all_links = []
# On average per page BF has 25 headlines, so to get around 1000 stories - I scraped 40 pages !

for i in range(1,41):
	# the url containing LGBT articles
	r = urllib.urlopen("https://www.buzzfeed.com/lgbt?p=%s&z=54UUHO&r=1"%str(i))
	# specify parser - lxml
	soup = BeautifulSoup(r, "lxml")
	# parse the class with the url
	links = soup.find_all("a", class_="lede__link")
	
	# capture the links from the parsed data
	links = map(lambda x: x["href"], links)
	# filter the empty urls
	links = filter(lambda x: x!='', links)
	# the links are repeated in the above class so we take only one
	links = links[0::2]
	all_links.append(links)


all_links = [item for sublist in all_links for item in sublist]
print all_links[:40]
with open(PIK, "w") as f:
	# store the list in a pickle file to load later !
    pickle.dump(all_links, f)
