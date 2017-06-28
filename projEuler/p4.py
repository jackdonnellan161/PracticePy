#! /usr/bin/env python3

#Statement: 

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

smallestNum = 100**2
largestNum = 999**2
pal = []
flag = False
def isPalindrome(num):
	aa = list(str(num))
	bb = aa[::-1]
	if aa == bb:
		return True
	else:
		return False

for numb in range(smallestNum,largestNum):
	if isPalindrome(numb):
		pal.append(numb)
pal = pal[::-1]

for num in pal:
	for ii in range(100,1000):
		if num%ii == 0:
			poss = num//ii
			possStr = list(str(poss))
			if len(possStr) == 3 and not flag:
				gotIt = num
				flag = True
print(gotIt)


