import sys
import os
import csv
from point import Point
from pointquadtree1 import *
from pointquadtree2 import *
from collections import Counter

f = file(sys.argv[1], 'rb')

rdr = csv.reader(f,delimiter=',')

header = rdr.next()

distanceKm = float(sys.argv[2])
distance = distanceKm * 0.009
data = []

for line in rdr:
	x = float(line[4])
	y = float(line[5])
	name = str(line[15])
	p = Point(x,y,name)
	data.append(p)

tree = pointquadtree(data)
counted = Counter(data)

def create_cluster(t, p, r, c):
	c.append(p)
	found = range_query(t, p, r)
	if (len(found) == 1 and len(c) != 1) or (len(found) == 0):
		return
	else:
		for point in found:
			if point not in c:
				create_cluster(t, point, r, c)

index = 1
os.mkdir("output")
while len(counted) != 0:
	clustered = []
	pt = list(counted.elements())[0]
	create_cluster(tree, pt, distance, clustered)
	counted -= Counter(clustered)

	if len(clustered) > 1:
		outputFile = "output\\" + str(index) + ".csv"
		out = open(outputFile, 'w')
		out.write("Name,X,Y\n")
		for j in clustered:
			out.write(j.name + "," + str(j.x) + "," + str(j.y) + "\n")
		out.close()
		index+=1
	
