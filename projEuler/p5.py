#! /usr/bin/env python3

#Statement:

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

masterFac = []

def primeFactors(num):
	factors = []
	while num !=1:
		for ii in range(2,num+1):
			if num%ii == 0:
				factors.append(ii)
				num = num//ii
#				print(factors,num)
				break
	return factors

for num in range(2,21):
	masterFac.append(primeFactors(num))

print(masterFac)

numTwos = 0
numThrees = 0
numFives = 0
numSevens = 0
numElev = 0
numThir = 0
numSeventeen = 0
numNineteen = 0

for prime in masterFac:
	for item in prime:
		if prime.count(2)>numTwos:
			numTwos = prime.count(2)
		if prime.count(3)>numThrees:
			numThrees = prime.count(3)
		if prime.count(5)>numFives:
			numFives = prime.count(5)
		if prime.count(7)>numSevens:
			numSevens = prime.count(7)
		if prime.count(11)>numElev:
			numElev = prime.count(11)
		if prime.count(13)>numThir:
			numThir = prime.count(13)
		if prime.count(17)>numSeventeen:
			numSeventeen = prime.count(17)
		if prime.count(19)>numNineteen:
			numNineteen = prime.count(19)

fin = numTwos*2 + numThrees*3 + numFives*5 + numSevens*7 + numElev*11 \
	+ numThir*13 + numSeventeen*17 + numNineteen*19

print(numTwos)
print(numThrees)
print(numFives)
print(numSevens)
print(numElev)
print(numThir)
print(numSeventeen)
print(numNineteen)

print(fin)




		
			

