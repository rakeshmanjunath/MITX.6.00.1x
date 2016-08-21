def howMany(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: int, how many values are in the dictionary.
	'''
	num=0
	for i in aDict:
		for j in aDict[i]:
			num+=1

	return num

def biggest(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: The key with the largest number of values associated with it
	'''
    
	big = None
	temp1 = 0
	temp2 = 0
	for i in aDict:
		temp1=0
		for j in aDict[i]:
			temp1+=1
		print temp1,temp2
		if(temp1>=temp2):
			big = i
			temp2=temp1
	
	return big
		
# numbers = {'e': [7, 11, 3, 4], 'G': [1, 12, 10, 6, 4], 'h': [20, 15, 1, 3], 'J': [1, 1, 17, 2], 'q': [12, 16], 'u': [], 't': []}
numbers ={'a': [2, 8, 4, 3, 3, 7], 'c': [20, 11, 16, 11, 15, 15, 0, 9, 5, 6], 'b': [2, 8, 17], 'd': [2, 5, 2, 7]}
# numbers = {'e': [], 'G': [],'u': [], 't': []}
print biggest(numbers)