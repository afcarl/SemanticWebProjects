#!usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
scraping the stories from the previously stored links
"""


import os,sys
import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import urllib
import pickle
import string
import re
printable = set(string.printable)

PIK = "pickle.dat"
PIK1 = "pickle1.dat"

# replace the new line and tab chars - we just need the content to build the NLP model+network
replace_them = ["  ","\n", "\t"]


# make the regex compiler
big_regex = re.compile('|'.join(map(re.escape, replace_them)))

with open(PIK, "r") as f:
	# load the links
    all_links = pickle.load(f)


stories = []
for link in all_links[:]:
	# read those links and scrape them - appending BF link before
	r = urllib.urlopen("https://www.buzzfeed.com"+link)
	# specify encoding as there are many non ascii chars can be present
	soup = BeautifulSoup(r, "lxml",from_encoding="utf-8")
	# extract the paragraphs
	content = soup.find_all("p")
	# specify while encoding too
	content = map(lambda x : big_regex.sub( ' ' ,x.get_text().strip().encode("ascii",errors='ignore')), content)
	# concatenate the list elements into a string
	stories.append(' '.join(content))





with open(PIK1,"w") as f:
	pickle.dump(stories,f)


print '\n'
print "DONE!\n"
