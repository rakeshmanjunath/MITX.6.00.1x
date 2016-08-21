
def dict_invert(d):
	'''input dict with immutable values (not list/dict).
	   returns inverse of the input dict. '''
	  
	d_out = {}
	for key in d:
		dout[d[key]].append(key)
	
	return d_out

d = {1:10, 2:20, 3:30}
print dict_invert(d)
d = {1:10, 2:20, 3:30, 4:30}
d = {4:True, 2:True, 0:True}