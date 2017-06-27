#!/usr/bin/env python3

from random import randint

def generate(number):
	possible = "abcdefghijklmnopqrstuvwxyz "
	posList = list(possible)
	generatedList = []
	for ii in range(number):
		kk = randint(0,26)
		generatedList.append(posList[kk])
	return generatedList;


goal = "methinks it is like a weasel"
list = generate(len(goal))
str = ''.join(list)
print(str)
print(goal)
