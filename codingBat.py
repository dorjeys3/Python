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
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a,b,negative):
	def pos_neg(a,b,negative):
	if negative:
		if a < 0 and b < 0:
			return True
		else:
			return False
	else:
		if a < 0 and b < 0:
			return False
		elif a < 0 or b < 0:
			return True
		else:
			return False

"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
	for i in range(0,len(str)):
		if str[0:3] == 'not':
			return str
		else:
			return "not " + str

"""

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
	toRemove = str[n]
	return str.replace(toRemove,"")


"""

Given a string, return a new string where the first and last chars have been exchanged. 

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

"""

def front_back(str):
	if len(str) <= 1:
	     return str

	mid = str[1:-1]
	
	return str[-1] + mid + str[0]


"""

Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. 

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
def front3(str):
	return str[:3] + str[:3] + str[:3]



#List - 1 ########################################################################################################
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
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. 

make_pi() → [3, 1, 4]

"""
def make_pi():
	return [3,1,4]

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

"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more. 

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""
def common_end(a,b):
	if( (a[0] == b[0]) or (a[-1] == b[-1])):
		return True
	else:
		return False

"""

Given an array of ints length 3, return the sum of all the elements. 

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""
def sum3(nums):
	sum = 0
	for i in nums:
		sum += i
	return sum

"""

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

def rotate_left3(nums):
  return [nums[1],nums[2], nums[0]]

"""

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}. 

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

"""
def reverse3(nums):
	return [nums[-1], nums[-2], nums[-3]]


"""

Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
def max_end3(nums):
	if nums[0] < nums[-1]:
		temp = nums[-1]
	else:
		temp = nums[0]

	return [temp,temp,temp]

"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0. 

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""

def sum2(nums):
	if(len(nums) == 0):
		return 0

	elif (len(nums) < 2):
		return nums[0]

	else:
		sum = 0
		sum = nums[1] + nums[0]
		return sum

"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
def middle_way(a,b):
	return [a[1],b[1]]


"""

Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more. 

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""
def make_ends(nums):
	return[nums[0],nums[-1]]

"""
iven an int array length 2, return True if it contains a 2 or a 3. 

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""
def has23(nums):
	if(nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3):
		return True
	else:
		return False


#String - 1 ########################################################################################################
"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!". 

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""
def hello_name(name):
	return "Hello " + name + "!"

"""
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi". 

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

"""
def make_abba(a,b):
	return a + b + b + a

"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>". 

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""
def make_tags(tag,word):
	return "<"+tag+">" + word + "</"+tag+">"



#Logic - 1 ########################################################################################################
"""

When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. 

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
def cigar_party(cigars,is_weekend):
	if(is_weekend and cigars >= 40):
		return True
	elif(cigars >= 40 and cigars <= 60):
		return True
	else:
		return False

"""

You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes.
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either 
of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe). 

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1

"""

def date_fashion(you,date):
	if(you =< 2 or date =< 2):
		return 0;
	elif(you >= 8 or date >= 8):
		return 2;
	else:
		return 1;
	






		

