def ndigits(x):	
	'''
	x: A positive or negative integer value.

	returns: int, number of digits in x.
	'''
	
	num =0
	x = abs(x)
	
	if x/10==0:
		return 1
	else:
		return 1 + ndigits(x/10)

print ndigits(6)
print ndigits(-33)
print ndigits(133)
