#! /usr/bin/env python3

''' 
Statement:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(num):
	for ii in range(2,num):
		if num%ii == 0:
			return False
			break
	return True

# is_prime tests:
# print(is_prime(10))
# print(is_prime(29))
# print(is_prime(2))


def num_prime(ii):
	num = 1
	counter = 0
	while counter != ii:
		num += 1
		if is_prime(num):
			counter += 1
	return num

print(num_prime(10001))
