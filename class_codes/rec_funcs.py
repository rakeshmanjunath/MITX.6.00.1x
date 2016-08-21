# Recursive Functions
"""
# Multiplication
def recMul(a,b):
  if(b==1):
    return a
  else:
    return a+ recMul(a,b-1)
	
# Factorial
def recFact(n):
  if n==1:
    return n
  return n*recFact(n-1)
"""

# Towers of Hanoi
def printMove(fr,to):
  print('move from %s to %s' %(fr,to))

def Towers(n,fr,to,sp):
  if n==1:
    printMove(fr,to)
  else:
    Towers(n-1,fr,sp,to)
    Towers(1,fr,to,sp)
    Towers(n-1,sp,to,fr)

# Palindrome Check
'''
def isPalindrome(s):
  def toChar(s):
    s=s.lower()
    ans=''
    for c in s:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans+=c
    return ans

  def isPal(s):
    if len(s)<=1:
      return True
    else:
      return s[0]==s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))
'''

def isPalindrome(aString):
  def toChar(aString):
    aString=aString.lower()
    ans=''
    for c in aString:
      if c in 'abcdefghijklmnopqrstuvwxyz':
        ans+=c
    return ans

  def isPal(aString):
    if len(aString)<=1:
      return True
    else:
      return aString[0]==aString[-1] and isPal(aString[1:-1])

    return isPal(toChar(aString))
