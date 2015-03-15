"""
Warmup - 1 sleep_in
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
Warmup - 2 sleep_in
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
Warmup - 3 sum_double

Given two int values, return their sum. Unless the two values are the same, then return double their sum. 

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
		

