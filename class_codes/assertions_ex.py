
def checkEq (a,b):
	try:
		assert a==b
	except AssertionError:
		print('AssertionError')