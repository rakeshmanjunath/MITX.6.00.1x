'''
Problem set 1-1
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
then your program should print Number of times bob occurs is: 2
'''

# s = 'azcbobobegghakl'
# s = 'bdfasdbobobofafewrbobwecdssubobobiouboiobobooubo'
s = 'bazcbobobegghabo'

count = 0

for ind in range(len(s)):
	if((ind>1) and (s[ind]+s[ind-1]+s[ind-2]=='bob')):
		count+=1

print 'Number of times bob occurs is: '+str(count)