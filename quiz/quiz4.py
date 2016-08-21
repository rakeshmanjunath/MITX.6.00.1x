
def f(a, b):
	# return a + b
	return a>b

def intersect(d1,d2):
	d3={}
	for i in d1:
		for j in d2:
			if i==j:
				d3[i]=f(d1[i],d2[i])
				break
	
	return d3

def difference(d1,d2):
	d4={}
	for i in d1:
		for j in d2:
			if i==j:
				break
		d4[i]=d1[i]
		d4[j]=d2[j]
	return d4
	
def dict_interdiff(d1,d2):
	'''
	d1, d2: dicts whose keys and values are integers
	Returns a tuple of dictionaries according to the instructions above
	'''
	
	d3={}
	for i in d1:
		for j in d2:
			if i==j:
				d3[i]=f(d1[i],d2[i])
				break
	
	d4 = {}
	for j in d1:
		if j not in d3:
			d4[j]=d1[j]
	
	for k in d2:
		if k not in d3:
			d4[k]=d2[k]
	
	return (d3,d4)

d1 = {1:30, 2:20, 3:30, 5:80, 7:100, 9:20}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print dict_interdiff(d1, d2)