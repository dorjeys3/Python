## Warmup - 1 #################################################
"""
sleep_in
The parameter weekday is True if it is a weekday, 
and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in. 
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def sleep_in(weekday, vacation):
	if vacation == True or weekday == False:
 		return True
 	else:
 		return False

"""
monkey_trouble
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of 
them is smiling. Return True if we are in trouble. 

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""
def monkey_trouble(a_smile, b_smile):
	if a_smile == b_smile:
		return True
	else:
		return False
"""
sum_double

Given two int values, return their sum. Unless the two values are the same, 
then return double their sum. 
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
def sum_double(a, b):
  if a != b:
  	return a+b
  else:
  	return 2*(a+b)

"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. 

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""
def parrot_trouble(talking,hour):
	if(talking == True and (hour <= 6 or hour >= 21)):
		return True
	else:
		return False


"""

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

"""

def makes10(a,b):
	sum = a + b
	if(a == 10 or b == 10 or sum == 10):
		return True
	else:
		return False

"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number. 

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
	withinCheck = (n % 100)
	if (withinCheck >= 90 or withinCheck <= 10) and n < 211 and n > 11:
		return True
	else:
		return False
"""

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. 

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""
def diff21(n):
  if abs(n) < 21
  	return abs(21 - n)
  else:
  	return 2*n


"""
NOT DONE
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a,b,negative):
	if a < 0 and b > 0 or a > 0 and b < 0:
		return True
	elif a < 0 and b < 0 and negative == False
		return True
	else
		return False


#List - 1 #####################################################
"""
first_last6
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more. 

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
def first_last6(nums):
	length = len(nums) - 1
	if nums[0] == 6 or nums[length] == 6:
		return True
	else:
		return False

"""
same_first_last
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal. 

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
def same_first_last(nums):
	if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
		return True
	else:
		return False

		

