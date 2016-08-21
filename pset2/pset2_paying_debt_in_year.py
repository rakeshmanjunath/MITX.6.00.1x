import time

start_time = time.time()
'''
# Test Case 1:
balance = 3329
annualInterestRate = 0.2

# Test Case 2:
balance = 4773
annualInterestRate = 0.2
'''

# Test Case 3:
balance = 3926
annualInterestRate = 0.2

monthlyInterestRate  = annualInterestRate/12.0
step                = 10
low_guess           = 0
rem_bal             = 1.0

def remaining_balance (balance,monthlyInterestRate,monthlyPayment):
	previousBalance     = balance
	for i in range(12):
		monthlyUnpaidBalance = previousBalance-monthlyPayment
		previousBalance      = monthlyUnpaidBalance*(1+monthlyInterestRate)
	return previousBalance

while (rem_bal>0):
	rem_bal=remaining_balance(balance,monthlyInterestRate,low_guess)
	low_guess +=  step

print 'Lowest Payment: '+ str(low_guess-step)

print 'Time taken: '+ str(time.time()-start_time)

