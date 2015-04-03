
#important imports
from sys import stdin
import math
#//////////////////////////////

#read array from stdin w/ spaces
inputArray = []
for element in input().split():
    inputArray.append(int(element))
#/////////////////////////////////

#read single value from stdin
singleInputVal = input()
#//////////////////////////////

#/////for i range(start,end,step)////////////
for i in range(start,-1,-1):
#//////////////////////////////

#//Read .txt each line with 2 arguments on each line////////////
from sys import stdin
file = open('gardenIn.txt', 'r') # readFile()
numberOfPoints = int(file.readline()) #cast for line to input

points =[]	# empty list
for ele in range(0,numberOfPoints,1):
	x,y = file.readline().strip().split() #fill list with 
	points.append([int(x),int(y)])

print(points) 
#//////////////////////////////////////////////////////////


#////Create decoding matrix///////////////////////////////
Matrix = [[0 for x in range(row)] for x in range(col)]
for i in range(col):
	print("\n") # newline
	for j in range(col):
		sys.stdout.write(" " + "(%s,%s)" % (i,j)) #print matrix

print("") #new line
#//////////////////////////////////////////////////