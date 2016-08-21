# Find Nth root

def findRoot(x,n,eps):
	"""finds nth root of x. x is a float. n in an int.
	eps is the accuracy and is float. returns 0 for imaginary nums"""

	if(x<0 and n%2==0):
		print('imaginary root, returns 0)
		return 0
	
	low = min(-1,x)
	high= max(1,x)
	ans = (high+low)/2.0
	
	while (abs(ans**n-x)-x)>=eps:
		print('high: %f, low: %f, ans: %f' %(high,low,ans))
		if ans**n<x:
			low=ans
		else:
			high=ans
		ans=(high+low)/2.0
	
	print('%dth root of number %f is approx. %f' (%n,x,ans))
	return ans

z=findRoot(x,n,eps)