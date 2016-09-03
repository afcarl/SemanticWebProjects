import os,sys
import pickle

PIK1 = "pickle1.dat"
PIK2 = "pickle2.dat"

PIK = "contentScraped.dat"

with open(PIK1, "r") as f:
	data1 = pickle.load(f)

with open(PIK2, "r") as f1:
	data2 = pickle.load(f1)

print data2[0]
print "\n"
print data1[0]

data = data1 + data2

with open(PIK, "w") as f:
	pickle.dump(data,f)


