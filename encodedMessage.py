#Problem >> https://open.kattis.com/problems/encodedmessage
import sys
import math

input = "eedARBtVrolsiesuAoReerles" #enter input string
length = len(input)
sqrtLength = int(math.sqrt(len(input)))
start = sqrtLength - 1

for i in range(start,-1,-1):  #for i range(start,end,step)
	for j in range(i,len(input),sqrtLength):
		sys.stdout.write(input[j])
				
		#sys.stdout.write(" " + "(%s,%s)" % (i,j)) #print matrix
print("")	