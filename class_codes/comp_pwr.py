# Computer powers using iteration

x = float(raw_input('Enter a number: ')
p = int(raw_input('Enter a integer power: ')

def itr_pwr(x,p):
	result=1
	for itr in range(p):
		result=result*x
		print('iteration: %d, Current Result: %f\n' %(itr,result))
	return result

z = itr_pwr(x,p)