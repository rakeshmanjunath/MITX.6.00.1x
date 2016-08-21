
def findPayment(loan,r,m):
	"""Assumes: loan and r(1.5%=0.015) are floats, m an int
	   Returns the monthly payment for a mortgage of size
	   loan at a monthly rate of r for m months"""
	return loan*((r*(1+r)**m)/((1+r)**m-1))

class Mortgage(object):
	"""Abstract class for building different kind of mortgages"""
	
	def __init__(self,loan,annRate,months):
		"""Create a new mortgage"""
		self.loan = loan
		self.rate = annRate/12.0
		self.months = months
		self.paid = [0.0]
		self.owed = [loan]
		self.payment = findPayment(loan,self.rate,months)
		self.legend = None #description of mortgage
	
	def makePayment(self):
		"""Make a payment"""
		self.paid.append(self.payment)
		reduction = self.payment-self.owed[-1]*self.rate
		self.owed.append(self.owed[-1]-reduction)
		
	def getTotalPaid(self):
		"""Return the total amount paid so far"""
		return sum(self.paid)
	
	def __str__(self):
		return self.legend
		
class FixedMortgage(Mortgage):
	def __init__(self,loan,annRate,months):
		"""Create Fixed Mortgage"""
		Mortgage.__init__(self,loan,annRate,months)
		self.legend = 'Fixed, '+str(annRate*100)+'%'
	
class FixedWithPtsMortgage(Mortgage):
	def __init__(self,loan,annRate,months,points):
		"""Create Fixed Mortgage with points"""
		Mortgage.__init__(self,loan,annRate,months)
		self.points=points
		self.paid = [loan*(points/100.0)]
		self.legend = 'Fixed points, '+str(annRate*100)+'% with'+str(points)+' points'
		
class TwoRateMortgage(Mortgage):
	def __init__(self,loan,annRate,months, teaserRate, teaserMonths):
		"""Create Two Rate Mortgage with teaserRate and teaserMonths"""
		Mortgage.__init__(self,loan,annRate,months)
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = annRate/12.0
		self.legend = 'Two rates ' + str(teaserRate*100)+'% for '+ \
		              str(self.teaserMonths)+ \
		              ' months, then '+str(annRate*100)+'%'
		
	def makePayment(self):
		if len(self.paid) == self.teaserMonths+1:
			self.rate=self.nextRate
			self.payment=findPayment(self.owed[-1],self.rate,
									 self.months - self.teaserMonths)
		
		Mortgage.makePayment(self)
	



	
