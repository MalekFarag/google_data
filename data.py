import csv 
import numpy as np
import matplotlib.pyplot as plt

categories = []
installs = []
ratings = []


with open("googeplaystore.csv") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0 

	for row in reader:
		if line_count is 0:
			print("pushing text to category array")
			categories.append(row)
			line_count += 1
		else :
			#print("collect the rest of the data")
			installdata = row[5]
			installdata = installdata.replace(",","")
			installdata = installdata.replace("Free", "0")
			installs.append(int(np.char.strip(installdata, "+")))
			line_count += 1 

print("processed", line_count, "rows of data")
print("first lne:", installs[0])
print("last line", installs[-1])
