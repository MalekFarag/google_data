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
			ratingsdata = row[2]
			ratingsdata = ratingsdata.replace("NaN", "0")
			ratings.append(float(ratingsdata))
			#print("collect the rest of the data")
			installdata = row[5]
			installdata = installdata.replace(",","")
			installdata = installdata.replace("Free", "0")
			installs.append(int(np.char.strip(installdata, "+")))
			line_count += 1 

print("processed", line_count, "rows of data")

print("Ratings: first lne:", ratings[0])
print("Ratings: last line", ratings[-1])

print("Installs: first lne:", installs[0])
print("Installs: last line", installs[-1])


np_ratings = np.array(ratings)
popular_apps = np_ratings > 4
pop_pct = len(np_ratings[popular_apps]) / len(np_ratings) * 100

print("Popular apps:")
print(pop_pct)

np_ratings = np.array(ratings)
unpopular_apps = np_ratings < 2
not_pop_pct = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100

print("Unpopular apps:")
print(not_pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)

print("Ok apps:")
print(mid_apps)



labels = "Bad, Ok, Good"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ["yellow", "red", "blue"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle= 140)
plt.axis = ("equal")

plt.legend(labels, loc=1)
plt.title("The good, the bad and the ok apps.")
plt.xlabel("User Ratings - Google Play Store Installs")
plt.show()
