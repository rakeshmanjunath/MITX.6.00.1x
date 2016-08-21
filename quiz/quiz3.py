
def flatten(aList):
	fList = []
	return flattenHelp(aList,fList)

def flattenHelp(aList,fList):
	for item in aList:
		if type(item)==list:
#			print item
			flattenHelp(item,fList)
		else:
			fList.append(item)
	
	return fList[:]

'''
def flatten(aList):
	for item in aList:
		if type(item)==list:
#			print item
			return flatten(item)
		else:
			return [item]
'''

print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print flatten([[1]])
print flatten([[1], [1]])
print flatten([[1], [2, 3]])