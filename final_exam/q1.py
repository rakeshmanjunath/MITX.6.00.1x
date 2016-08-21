
def dict_invert(d):
	'''input dict with immutable values (not list/dict).
	   returns inverse of the input dict. '''
	  
	d_out = {}
	for key in d:
		d_out[d[key]] = []
	
	for key in d:
		d_out[d[key]].append(key)
	
	for key in d:
		d_out[d[key]].sort()

	return d_out

d = {1:10, 2:20, 3:30}
print dict_invert(d)
d = {1:10, 2:20, 3:30, 4:30}
print dict_invert(d)
d = {4:True, 2:True, 0:True}
print dict_invert(d)
print dict_invert({8: 6, 2: 6, 4: 6, 6: 6})


