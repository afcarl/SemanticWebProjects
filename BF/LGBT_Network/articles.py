#!/usr/bin/python27
# -*- coding: <utf8> -*-

import os,sys
import numpy as np 
import pandas as pd 
import gensim
import nltk
from nltk.corpus import stopwords
import pickle
from gensim import corpora, models, similarities
from nltk.tokenize import sent_tokenize
import re
import string


PIK = "pickle1.dat"

def get_tags(contains_tags):
	"""
	get tags from the articles
	"""
	sent_tokenize_list = sent_tokenize(contains_tags)
	filtered_tags = filter(lambda x: "Tagged" in x, sent_tokenize_list)
	filtered_tags = map(lambda x: x.split("by")[0] if ("by" in x) else x, filtered_tags)
	print filtered_tags



with open(PIK, "r") as f:
	data = pickle.load(f)

documents = []

for i in range(20):
	#print i
	#print type(data[i])
	elems = data[i].split("Check out more articles on BuzzFeed.com!")
	documents.append(elems[0])
	

punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]

for d in documents:
	d = d.lower()
	d = punc.sub("",d)
	term_vec.append(map (lambda x: unicode(x,errors="ignore"), nltk.word_tokenize(d)))



stop_words = nltk.corpus.stopwords.words("english")


for i in range(0,len(term_vec)):
	term_list = []

	for term in term_vec[i]:
		if term not in stop_words:
			term_list.append(term)


	term_vec[i] = term_list



dict = gensim.corpora.Dictionary(term_vec)
corp = []
for i in range(0,len(term_vec)):
	corp.append(dict.doc2bow(term_vec[i]))

#  Create TFIDF vectors based on term vectors bag-of-word corpora

tfidf_model = gensim.models.TfidfModel(corp)

tfidf = []
for i in range(0,len(corp)):
	tfidf.append(tfidf_model[corp[i]])


model = models.LdaModel(corp, id2word=dict, num_topics=5)
print model.print_topics()