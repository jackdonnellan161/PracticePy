#! /usr/bin/env python3

#Statement: 

#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squareList(x):
	square = [ii**2 for ii in x]
	return square

def sumList(nat):
	tot = 0
	if len(nat) == 1:
		tot = nat[0]
	else:
		tot = nat[0]+sumList(nat[1:])
	return tot

nums = list(range(1,101))
ans = sumList(squareList(nums))-(sumList(nums)**2)
if ans<0:
	ans = -ans
print(ans)
