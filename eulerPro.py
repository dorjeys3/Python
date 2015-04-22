import sys
import math
from collections import OrderedDict

#1 Multiples of 3 and 5
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def multThreeOrFive():
	sum = 0
	for i in range(0, 1000):
		if((i%5 == 0) or (i%3 == 0)): # check if muliple of 3 or 5 
			sum += i  # if so add value to sum
	return sum

#2 Even Fibonacci Numbers
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def fib(n):				#recursively defining fibonacci sequence
	if(n == 0):
		return 0
	elif(n <= 2):
		return 1
	else:
		return fib(n-1) + fib(n-2)


def evenFibonacciSum():
	sum = 0
	i = 0
	while True: # go thru sequence
		if(fib(i) >= 4000000):  # break if sequence reach 4mil
			break
		elif(fib(i)%2 == 0):	#if even add to rolling sum
			sum += fib(i)
		i += 1 #i++
	return sum

#3 Largest Prime Factor
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def largestPrime(n):
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1
	return n

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def LargestPalindrome(n):
	numbers = []
	for i in range(900,999):
		for j in range(900,999):
			product = str(i*j)
			if(product[0] == product[-1] and product[1] == product[-2] and product[2] == product[-3]):
				max = i*j
	return max



			


#//////////////////////Write Under Here//////////////////////////////////////
print("Answer:")
print(LargestPalindrome(1))
sys.exit()