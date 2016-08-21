
# Read value

def readVal(valType,requestMsg,errorMsg):
	while True:
		val=raw_input(requestMsg+' ')
		try:
			val=valType(val)
			return val
		except ValueError:
			print(val+' '+errorMsg)
			
# z= readVal(int,'EnterInt','ErrorInt')

def getRatios(vec1,vec2):
	"""Assumes:vec1 and vec2 are list of equal length of numbers
	   Returns:A list containing meaningful values of vec1[i]/vec2[i]"""
	   
	ratios=[]
	for i in range(len(vec1)):
		try:
			ratios.append(vec1[i]/float(vec2[i]))
		except ZeroDivisionError:
			ratios.append(float('nan')) # nan = not a number
		except:
			raise ValueError('getRatios called with bad args')
	return ratios

"""
v1 = [1,0,-3,4.4]
v2 = [0,4,3,2]
v3 = [1,2,3,'abc']
v4 = [1,2,3]

try:
	print(getRatios(v1,v2))
#	print(getRatios(v1,v3))
	print(getRatios(v1,v4))
except ValueError, msg:
	print msg
"""

def getGrades(fname):
	try:
		gradesFile = open(fname, 'r') # open fname file pointing at r
	except IOError:
		raise ValueError('getGrade could not open '+fname)
	
	grades = []
	# print gradesFile
	
	for line in gradesFile:
		# print line
		try:
			grades.append(float(line))
		except:
			raise ValueError('Unable to convert	line to float')
	return grades

"""
try:
	grades = getGrades('quiz1grades.txt')
	print grades
	grades.sort()
	median=grades[len(grades)/2]
	print 'Median grade is ',median
except ValueError, errorMsg:
	print 'Whoops.', errorMsg
"""

