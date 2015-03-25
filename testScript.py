def near_hundred(n):
	withinCheck = (n % 100)
	if (withinCheck >= 90 or withinCheck <= 10) and n < 211 and n > 11:
		return True
	else:
		return False
