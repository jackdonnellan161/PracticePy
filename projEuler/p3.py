#! /usr/bin/env python3

#Statement: 

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

num = 600851475143
high = 0


def primeFactor(limit):
	tot = limit
	for ii in range(2,tot):
		if tot%ii == 0:
			tot = tot//ii
			print([ii,tot])
			return [ii,tot]
	return False

print(primeFactor(6857))
print(num%6857)

aa = primeFactor(num)
high = aa[0]
while aa[1] != 1:
	aa = primeFactor(aa[1])
	if aa[0]>high:
		high = aa[0]
print(aa)
