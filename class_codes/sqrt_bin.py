# Binary Search Square root code

x=25
eps=0.01
num_guess=0
low=0.0
high = x
ans = (high+low)/2.0

while abs(ans**2-x)>=eps:
	print ('low = %f, high = %f, ans = %f' %(low, high, ans))
	num_guess +=1
	if ans**2 < x:
		low=ans
	else:
		high=ans
	ans=(high+low)/2.0
print('num_guess = %f' %num_guess)

print('%f is close to square root of %f' %(ans, x))