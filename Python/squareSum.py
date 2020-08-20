'''
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sumOfSquares = 0
squareOfSums = 0
amount = 100

# sum of squares
# 1^2+2^2...+100^2
for i in range(amount + 1):
    sumOfSquares += i**2
    if (i == 0): continue

# square of sums
# (1+2+...+100)^2
for i in range(amount + 1):
    squareOfSums += i
    if (i == 0): continue
squareOfSums **= 2

# output the difference
# |x - y|
print(abs(squareOfSums - sumOfSquares))