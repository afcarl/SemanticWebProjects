import os,sys
import pickle

with open("pickle1.dat","r") as f:
	data = pickle.load(f)

print data[0]