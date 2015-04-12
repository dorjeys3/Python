
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
<<<<<<< HEAD
#///////////////////////////////////////////
=======
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

# sort string entry
a = ''.join(sorted(num2))
b = ''.join(sorted(num1))   

#////Create decoding matrix///////////////////////////////
Matrix = [[0 for x in range(row)] for x in range(col)]
for i in range(col):
	print("\n") # newline
	for j in range(col):
		sys.stdout.write(" " + "(%s,%s)" % (i,j)) #print matrix
>>>>>>> 7d45fcafbb7406097e7b117fbd17c35f39cefd15

