
#important imports
from sys import stdin
import math
#//////////////////////////////

def readLine(length):  #Read in a line from txt >> List
	file = open("input.txt", 'r')
	inputArray = []
	for element in range(0,length):
		a,b,d,e,f = file.readline().strip().split()
    	inputArray.append([a,b,c,d,e,f])
    			#input.txt
    			""" 1 2 3 4 5

 		   	 	"""
 		   		#inputArray = [1,2,3,4,5]

def readSingle(): 		
	singleInputVal = input() #Read in single input(Cin >> variable [c++])
	fileSingleInput = file.readline() # Read line from file

def createMatrix(row,col):
#////Create decoding matrix///////////////////////////////
	Matrix = [[0 for x in range(row)] for x in range(col)]
	for i in range(col):
		print("\n") # newline
		for j in range(col):
			sys.stdout.write(" " + "(%s,%s)" % (i,j)) #print matrix
		print("") #new line
#//////////////////////////////////////////////////

#/////for i range(start,end,step)////////////
for i in range(start,-1,-1):
#///////////////////////////////////////////

