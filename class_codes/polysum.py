
from math import *

def polysum (n,s):
	'''
	Takes: n - number of sides, s - side length.
	Computes: Area+perimeter^2
	'''
	area = (0.25*n*s*s)/tan(pi/n)
	perimeter = n*s
	print area
	print perimeter
	return round(area+perimeter**2,4)

