
# stuff = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
# stuff = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
# stuff = "iQ"

# stuff = ["iQ"]
# stuff = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# stuff = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]


# for thing in stuff:
#	if thing == 'iQ':
#		print "Found it"
		

# def Square(x):
#     return SquareHelper(abs(x), abs(x))

# def SquareHelper(n, x):
#     if n == 0:
#        return 0
#     return SquareHelper(n-1, x) + x

# print Square(5)
# print Square(-7)
# print Square(-2)
# print Square(0)
# print Square(-0.5)
# print Square(0.1)

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
	
print isPalindrome('')
print isPalindrome('GOoAw')
print isPalindrome('JJXJJ')