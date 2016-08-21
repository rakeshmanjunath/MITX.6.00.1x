
def nfruits(fruitDict, fruitPattern):
	"""
	fruitDict: Dictionary, Key is fruit name (capital letter),
	Value is initial value of fruits Python starts with.
	
	fruitPattern: String, Pattern with which Python eats fruits
	until he reaches MIT
	
	returns maxValFD: integer, maximum quantity out of the 
	different types of fruits.
	"""
	
	lenFP    = len(fruitPattern)
	maxValFD = 0
	
	# For all fruits eaten except last one
	for i in range(lenFP-1):
		for key in fruitDict:
			if key==fruitPattern[i]:
				fruitDict[key]-=1
			else:
				fruitDict[key]+=1
	
	# Last fruit eaten
	for key in fruitDict:
		if key==fruitPattern[-1]:
			fruitDict[key]-=1
	
	# Finding max value in the fruitDict
	for key in fruitDict:
		if fruitDict[key]>maxValFD:
			maxValFD=fruitDict[key]
	
	return maxValFD

print nfruits({'A': 1, 'B': 2, 'C': 3},'AC')
print nfruits({'I': 9, 'S': 7, 'J': 8, 'V': 6}, 'S')