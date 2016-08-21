
def dotProduct(listA, listB):
	'''
	listA: a list of numbers
	listB: a list of numbers of the same length as listA
	'''
	
	acc = 0
	
	for idx in range(len(listA)):
		acc+=listA[idx]*listB[idx]
	
	return acc
	
print dotProduct([1, 2, 3], [4, 5, 6])
print dotProduct([5, 6, 7], [5, 6, 7])