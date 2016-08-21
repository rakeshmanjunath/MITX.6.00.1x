
# Tuple Example
def findDivisors(n1,n2):
	"""assumes n1 and n2 are +ve integers.
	returning tuple contains common divisors"""
	
	divisors()
	for i in range(1,min(n1,n2)):
		if n1%i==0 and n2%i==0:
			divisors=divisors+(i,)
	
	return divisors

x = ['abc','def','ghi']
y = ['abd','deg','ghj']
x.append('app')
z = [x,y,'mno']

for e in z:
	print e
	for u in e:
		print u

# Below code doesn't work as expected
for e1 in L1:
	if e1 in L2:
		L1.remove(e1)

# Fix
L1Clone = L1[:]

for e1 in L1Clone:
	if e1 in L2:
		L1.remove(e1)

