#!/usr/bin/python27
# -*- coding: <utf8> -*-

import os,sys
import numpy as np 
import pandas as pd 
import gensim
import nltk
from nltk.corpus import stopwords
import pickle
from collections import Counter
from gensim import corpora, models, similarities
from nltk.tokenize import sent_tokenize
import re
import string
import collections
import itertools

PIK = "contentScraped.dat"

def get_tags(contains_tags):
	"""
	get tags from the articles
	"""
	sent_tokenize_list = sent_tokenize(contains_tags)
	filtered_tags = filter(lambda x: "Tagged" in x, sent_tokenize_list)
	filtered_tags = map(lambda x: x.split("by")[0] if ("by" in x) else x, filtered_tags)
	filtered_tags = map(lambda x: x.split(":",1)[1], filtered_tags)
	if filtered_tags!=[]:

		filtered_tags = map(lambda x: x.split(","), filtered_tags)[0]

		
		for t in filtered_tags[-1:]:
			
			if "Hey" in t:
				filtered_tags[-1] = t.split("Hey",1)[0]
				

		filtered_tags = map(lambda x: x.strip(), filtered_tags)


		
		return filtered_tags

	else:
		return []



with open(PIK, "r") as f:
	data = pickle.load(f)

document_tags = []


for i in range(len(data)):
	#print i
	#print type(data[i])
	elems = data[i].split("Check out more articles on BuzzFeed.com!")
	document_tags.append(elems[1])
	
tags = map(lambda x: get_tags(x), document_tags)
tags = filter(lambda x: x!=[],tags)
tags = [item for sublist in tags for item in sublist]
print len(tags)

counter_per_word = Counter(tags)

with open("counter_per_word.dat", "w") as f:
	pickle.dump(counter_per_word,f)


combinations = []

for tag in tags:
	comb_set = map(lambda x: set(x), itertools.combinations(tag,2))

	comb_ls = map(lambda x: tuple(x), comb_set)
	
	combinations.append(comb_ls)



combinations = [item for sublist in combinations for item in sublist]
#print combinations
print '\n'
counter_pairs = Counter(combinations)

PIK_Pairs = 'counter_pairs.dat'

with open(PIK_Pairs, "w") as f:
	pickle.dump(counter_pairs,f)

to_consider_pairs = [k for k, v in Counter(combinations).iteritems() if v > 4 ]
print to_consider_pairs
