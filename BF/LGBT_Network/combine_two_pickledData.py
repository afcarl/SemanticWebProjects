import os,sys
import pickle

PIK1 = "pickle1.dat"
PIK2 = "pickle2.dat"

with open(PIK1, "r") as f:
	data = pickle.load(f)

with open(PIK2, "r") as f1:
	data1 = pickle.load(f1)

print data[0]
print "\n"
print data1[0]
