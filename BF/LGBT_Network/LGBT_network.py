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
import json
import networkx

PIK_pairs = "counter_pairs.dat"
PIK_words = "counter_per_word.dat"

with open(PIK_pairs, "r") as f:
	data = pickle.load(f)

with open(PIK_words, "r") as f:
	word_count = pickle.load(f)



value = [v for k,v in word_count.iteritems() if v>10]

to_consider_pairs = [k for k, v in data.iteritems() if v > 10 ]
print to_consider_pairs
source = map(lambda x: x[0], to_consider_pairs)
target = map(lambda x: x[1:], to_consider_pairs)


print ([v for k, v in data.iteritems() if v > 10 ])
nodes_ls = list(set([item for sublist in to_consider_pairs for item in sublist]))
print nodes_ls


# creating the json file

nodes = []

for n in nodes_ls:
	nodes.append({"id":str(n), "group": 1})

links = []

for s,t,v in zip(source,target,value):
	links.append({"source": str(s), "target": str(t), "value": v})


opFile = {}

opFile["nodes"] = nodes
opFile["links"] = links

json_data = json.dumps(opFile)


with open('data.txt', 'w') as outfile:
    json.dump(json_data, outfile)










