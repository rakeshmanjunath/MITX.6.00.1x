# Decimal to binary floating point

x = float(raw_input('Enter a decimal number between 0 & 1:'))

p=0

while ((2**p)*x)%1 != 0:
	print('remainder =' + str((2**p)*x-int((2**p)*x))) 
	p += 1

num = int((2**p)*x)
print ('p value is ' + str(p))
print ('num value is ' + str(num))

result = ""

if num == 0:
	result='0'
while num > 0:
	result = str(num%2) + result
	num = num/2

print('inter result1 ' + str(result))

for i in range (p-len(result)):
	result = '0' + result

print('inter result2 ' + str(result))
print('inter result3 ' + str(result[0:-p]))
print('inter result4 ' + str(result[-p:]))

result = result[0:-p]+ '.' + result[-p:]


print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
