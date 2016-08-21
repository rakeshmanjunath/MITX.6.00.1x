
# s is a string of lower case characters.
# counts number of vowels in the string s
# Valid vowels: a,e,i,o,u
# Ex: s = 'azcbobobegghakl' your program should print: 'Number of vowels: 5'
# s is already provided. 

# String -> Number

s = 'azcbobobegghakl'
s = 'adfasdfafewrwecdssuiouiouio'
count = 0

for ltr in s:
	if(ltr=='a' or ltr=='e' or ltr=='i' or ltr=='o' or ltr=='u'):
		count=count+1

print 'Number of vowels: '+str(count)

