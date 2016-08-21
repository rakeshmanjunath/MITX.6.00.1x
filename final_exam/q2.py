
def getSublists(L, n):
	'''L is not empty
	   0 < n < len(L)'''
	
	K = []
	for i in range(len(L)-n+1):
		M = []
		for j in range(i,i+n):
			M.append(L[j])
		K.append(M)
	
	return K

'''
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
print getSublists(L, n)
L = [1, 1, 1, 1, 4]
n = 2
print getSublists(L, n)
'''

def longestRun(L):
	
	for i in range(len(L),0,-1):
		M = getSublists(L,i)
		for N in M:
			if (sorted(N) == N):
				return i
	
	return None

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print longestRun(L)