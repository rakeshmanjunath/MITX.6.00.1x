# Hash Table example - Hash function i%j 
# Using Hash table we can decrease search time to O(1)+O(x) - x<<n
# This can be done only when we know probaility of key occurence.
# Like A-law,U-law - more num buckets for more probable key values

import random

class intDict(object):
	"""A dictionary with integer keys"""
	
	def __init__(self,numBuckets):
		"""Create an empty dictionary"""
		self.buckets=[]
		self.numBuckets= numBuckets
		for i in range(numBuckets):
			self.buckets.append([])
	
	def addEntry(self,dictKey,dictVal):
		"""Assumes dictkey an int. Adds an entry."""
		hashBucket = self.buckets[dictKey%self.numBuckets]
		
		# If key already has value udpate value
		for i in range(len(hashBucket)):
			if hashBucket[i][0]==dictKey:
				hashBucket[i]=(dictKey,dictVal)
				return
		
		# Add new Key-value pair
		hashBucket.append((dictKey,dictVal))
	
	def getValue(self,dictKey):
		"""Assumes dictKey an int. Returns entry associated
		   with the key dictKey."""
		hashBucket = self.buckets[dictKey%self.numBuckets]
		for e in hashBucket:
			if e[0]==dictKey:
				return e[1]
			return None
	
	def __str__(self):
		res = '{'
		for b in self.buckets:
			for t in b:
				res = res+str(t[0])+':'+str(t[1])+','
		return res[:-1]+'}'

# Example usage
D = intDict(29)

for i in range(20):
	# Choose a random int between 0 and 10**5
	key = random.randint(0,10**5)
	D.addEntry(key,i)

print 'The value of the intDict is:'
print D
print '\n','The buckets are:'

# Accesing internal buckets for visualization purposes
for hashBucket in D.buckets:
	print ' ',hashBucket

