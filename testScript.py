import sys

def common_end(a,b):
	if( (a[0] == b[0]) or (a[-1] == b[-1])):
		print(a[-1])
		return True
	else:
		return False


print common_end([3,1,4],[2,2,2])