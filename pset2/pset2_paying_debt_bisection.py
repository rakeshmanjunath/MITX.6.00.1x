import time

start_time = time.time()
'''
# Test Case 1:
balance = 320000
annualInterestRate = 0.2
#-------------------
#Lowest Payment: 29157.09

'''
# Test Case 2:
balance = 999999
annualInterestRate = 0.18
#-------------------
#Lowest Payment: 90325.03


monthlyInterestRate  = annualInterestRate/12.0
low_guess           = balance/12.0
high_guess          = balance*((1+monthlyInterestRate)**12)/12.0
guess               = (low_guess+high_guess)/2.0
rem_bal             = 1.0

def remaining_balance (balance,monthlyInterestRate,monthlyPayment):
	previousBalance     = balance
	for i in range(12):
		monthlyUnpaidBalance = previousBalance-monthlyPayment
		previousBalance      = monthlyUnpaidBalance*(1+monthlyInterestRate)
	return previousBalance

while True:
	rem_bal=remaining_balance(balance,monthlyInterestRate,guess)
	if(rem_bal>0.01):
		low_guess=guess
	elif (rem_bal<-0.01):
		high_guess=guess
	else:
		break
	guess = (high_guess+low_guess)/2.0

end_time = time.time()

print 'Lowest Payment: '+ str(round(guess,2))

print 'Time taken: %f' %(end_time-start_time)

