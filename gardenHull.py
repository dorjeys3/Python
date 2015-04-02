from sys import stdin

file = open('gardenIn.txt', 'r')

numberOfPoints = file.readline()

points = [] 

for x,y in file.readlines():
	points.append([x,y])

print(numberOfPoints)