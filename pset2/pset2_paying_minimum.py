'''
# Test 1
balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04
'''

# Test 2
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
previousBalance     = balance
Total_paid          = 0

for i in range(12):
	minimumMonthlyPayment = monthlyPaymentRate*previousBalance
	monthlyUnpaidBalance  = previousBalance-minimumMonthlyPayment
	previousBalance       = monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
	Total_paid += minimumMonthlyPayment
	print 'Month: '+str(i+1)
	print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2))
	print 'Remaining balance: ' + str(round(previousBalance, 2))

print 'Total paid: '+str(round(Total_paid,2))
print 'Remaining balance: '+str(round(previousBalance,2))