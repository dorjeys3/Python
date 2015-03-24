
#important imports
from sys import stdin
import math

#read array from stdin w/ spaces
inputArray = []
for element in input().split():
    inputArray.append(int(element))
#/////////////////////////////////

#read single value from stdin
singleInputVal = input()
#//////////////////////////////


#set up row and col for matrix
row = 4
col = 4
#Create decoding matrix
Matrix = [[0 for x in range(row)] for x in range(col)]
for i in range(col):
	print("\n") # newline
	for j in range(col):
		sys.stdout.write(" " + "(%s,%s)" % (i,j)) #print matrix

print("")	