<<<<<<< HEAD

=======
import sys
import math

#sortingAlgo
def mergeSort(str):
	#divide
	#div2 = divide(1)
	return list(str)

def divide(toBreak):
	if len(toBreak)%2 == 0:
		midPoint = int((len(toBreak))/2)
	else:
		midPoint = int((len(toBreak)-1)/2)
	first = toBreak[:midPoint]
	second = toBreak[midPoint:]
	return [first,second]


#////Main///////////////////
file = open("input.txt",'r')

num1 = file.readline()
num2 = file.readline()

print(mergeSort(num1))

	
"""
#call mergesort
a = mergeSort(num2)
b = mergeSort(num1)

print(a)
print(b)


#same length
if len(num1) == len(num2):
	for i in range(0,len(num1)):
		if a[i] != b[i] and a[i] > b[i]:
			print(num2)
		elif a[i] != b[i] and b[i] > a[i]:
			print(num1)

#case for different length
else:
	if int(a) > int(b):
		print(num2)
	else:
		print(num1) 
"""
#timeComplex
#https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
>>>>>>> 7d45fcafbb7406097e7b117fbd17c35f39cefd15
