
print 'Please think of a number between 0 and 100!'

is_corr=''
high=100
low=0

while is_corr!='c':
	guess=(high+low)/2
	
	print "Is your secret number " + str(guess) + "?."
	print "Enter 'h' to indicate the guess is too high.",
	print "Enter 'l' to indicate the guess is too low.",
	is_corr = raw_input("Enter 'c' to indicate I guessed correctly.")

	if is_corr=='h':
		high=guess
	elif is_corr=='l':
		low=guess
	elif is_corr=='c':
		print 'Game over. Your secret number was: '+str(guess)
	else:
		print 'Sorry, I did not understand your input.'



#	print "Enter 'h' to indicate the guess is too high.",
#	print "Enter 'l' to indicate the guess is too low.",
#	print "Enter 'c' to indicate I guessed correctly."
#	is_corr = raw_input()