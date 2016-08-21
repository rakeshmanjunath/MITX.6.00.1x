# nwtn raphson squrt method

eps=0.01
y=1234567.0
g=y/2.0
num_guess=0

while abs(g*g-y) >= eps:
	g=g-(g**2-y)/(2*g)
	num_guess +=1
	
print ('square root of %f is about %f, found using %d guesses' %(y, g, num_guess))
