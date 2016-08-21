from find_payment import *

def compareMortgages(amt, years, fixedRate, pts, ptsRate, 
                     varTeaserRate, varFinRate, varMonths):
	
	totMonths = years*12
	fixed1 = FixedMortgage(amt, fixedRate, totMonths)
	fixed2 = FixedWithPtsMortgage(amt, ptsRate, totMonths, pts)
	tworate= TwoRateMortgage(amt, varFinRate, totMonths, varTeaserRate,
                             varMonths)	
	
	morts = [fixed1, fixed2, tworate]
	
	for m in range(totMonths):
		for mort in morts:
			mort.makePayment()
		
		for m in morts:
			print str(m) + ' Total Payments = '+str(int(m.getTotalPaid()))
	

compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25,
                 ptsRate=0.05, varTeaserRate=0.045, varFinRate=0.095,
				 varMonths=48)

