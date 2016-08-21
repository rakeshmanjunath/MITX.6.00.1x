'''
x=3
y=str(x)
print (y+' is a string')
ans=0
i=x
while(i!=0):
	ans=ans+x
	i=i-1
print (str(x)+'*'+str(x)+'='+str(ans))


def max (x,y):
	if x>y:
		return x
	else:
		return y

z = max(3,4)

print('max value %d' %z)
'''

def iterPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0
 
	returns: int or float, base^exp
	'''
	result = 1
	for i in range(exp):
		result = result*base

	return result

#print iterPower(2,3)
#print iterPower(3,4)
#print iterPower(4,4)
#print iterPower(1.1,2)

def recurPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0

	returns: int or float, base^exp
	'''
	if exp==1:
		return base
	else:
		return base * recurPower(base, exp-1)
		

#print recurPower(2,3)
#print recurPower(3,4)
#print recurPower(4,4)
#print recurPower(1.1,2)

def recurPowerNew(base, exp):
	'''
	base: int or float.
	exp: int >= 0

	returns: int or float, base^exp
	'''
	if exp>0  and exp%2==0:
		return recurPowerNew(base*base, exp/2)
	elif exp>0 and exp%2!=0:
		return base * recurPowerNew(base, exp-1)
	else:
		return 1
		
#print recurPowerNew(2,3)
#print recurPowerNew(3,5)
#print recurPowerNew(4,3)
#print recurPowerNew(5,4)
#print recurPowerNew(1.1,2)
#print recurPowerNew(2,4)
#print recurPowerNew(7,2)

def gcdIter(a, b):
	'''
	a, b: positive integers

	returns: a positive integer, the greatest common divisor of a & b.
	'''
	les_val = min(a,b)
	while les_val>1:
		if a%les_val==0 and b%les_val==0:
			return les_val
		les_val-=1
	
	return les_val

# print gcdIter(3,6)
# print gcdIter(12,16)
# print gcdIter(7,11)

def gcdRecur(a, b):
	'''
	a, b: positive integers

	returns: a positive integer, the greatest common divisor of a & b.
	'''
	
	if b==0:
		return a
	else:
		return gcdRecur(b,a%b)
		
# print gcdRecur(3,6)
# print gcdRecur(12,16)
# print gcdRecur(7,11)

def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string

	returns: True if char is in aStr; False otherwise
	'''
	length = len(aStr)
	
	if length==1 and char!=aStr:
		return False
	elif char==aStr[length/2]:
		return True
	elif char>aStr[length/2]:
		return isIn(char, aStr[length/2+1:])
	elif char<aStr[length/2]:
		return isIn(char, aStr[0:length/2])

print isIn('a','abc')
print isIn('b','abc')
print isIn('w','w')
print isIn('x','stuvwx')
print isIn('p','abcd')
print isIn('i','ghijk')