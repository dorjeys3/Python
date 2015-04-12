from sys import stdin
import math

file = open('gardenIn.txt', 'r')

numberOfPoints = int(file.readline()) #Parse inputs
points = []
for ele in range(0,numberOfPoints):
	x,y = file.readline().strip().split()
	points.append([int(x),int(y)])

points.sort() # least to greatest
start = points[0]
trip = [start]

for i in range(0,len(points)):
	x1 = points[i][0]
	y1 = points[i][1]
	x2 = points[i+1][0]
	y2 = points[i+1][1]	

	if x1 == x2:
		slope = y2 - y1 #distance for between y
	else:
		slope = (y2-y1)/(x2-x1) #distance between points

	if slope > 0: # leftTurn
		trip.append([x2,y2])

	else:
		trip.append
		

a = math.pow(x2 - x1)
		b = math.pow(y2 - y1)
		distance = math.sqrt(a + b)



"""	
distance = math.sqrt()
	#leftTurn (+slope)
	if slope > 0

	#rightTurn
	else
"""
