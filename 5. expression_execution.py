# expression execution 

# string and numeric value can be operate with *
a,b = 2,3
text = "@"
print(a*text*b)

# string and string can operate with +
a = 5
b = '3'
text = '%'
print((b+text)*a)

# number to number operation 
d = 3
e = 2
calculate = e**d

# '**' means power in mathematics
print('the value of d is : ',d)
print('the value of e is : ',e)
print('the result of e**d is : ',calculate)
print('the sum of d and e is : ',d + e)
print('the difference of d and e is : ',d - e)
print('the multiplication of d and e is : ',d * e)
print('the division of d and e is : ',d / e)
print('the result of (d + e * d) : ',d+e*d)
print('------------------------------------')

# the arithematic operation of integer and float will always be float
a = 1
b = 2.2
print('the result of a + b is : ',a+b)
print('the result of a - b is : ',a-b)
print('the result of a * b is : ',a*b)

print('---------------------------------')
# the result of division operator with two integers will be float
a = 12
b = 21
print('the result of a/b is : ',a/b)

print('---------------------------------')
# Remainder is negative when only denomenator is negative
a = 10
b = -22
c = a % a
d = b % b
e = a % b
f = b % a 
print('the result of c is : ',c)
print('the result of d is : ',d)
print('the result of e is : ',e)
print('the result of f is : ',f)