"""
Assumes L is a list of strings
Assume function f is already defined for you and it maps a string to a Boolean
Mutates L such that it contains all of the strings, s, originally in L such
that f(s) returns True, and no other elements. Remaining elements in L
should be in the same order.
Returns the length of L after mutation
"""

def f(s):
	return 'a' in s
	
def satisfiesF(L):
	G = L[:]
	j=0
	for i in range(len(G)):
		if not f(G[i]):
			del L[i-j]
			j+=1

	return len(L)

run_satisfiesF(L, satisfiesF)

# Add my own test cases here.
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

L = []
print satisfiesF(L)
print L

L = ['a']
print satisfiesF(L)
print L

L = ['c', 'b', 'a']
print satisfiesF(L)
print L

L = ['s', 'q', 'e']
print satisfiesF(L)
print L