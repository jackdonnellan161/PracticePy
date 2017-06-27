#!/usr/bin/env python3

from random import randint

def generate(number):
	possible = "abcdefghijklmnopqrstuvwxyz "
	posList = list(possible)
	generatedList = []
	for ii in range(number):
		kk = randint(0,26)
		generatedList.append(posList[kk])
		generated = ''.join(generatedList)
	return generated;

def check(generated,goal):
	ii=0
	count = 0
	total = len(generated)
	if len(generated) != len(goal):
		raise RuntimeError("Something went wrong!")
	else:
		while ii<total:
			if generated[ii] == goal[ii]:
				count = count+1
				print(ii+1)
			ii = ii+1
	print(count, total)
	
	return 0

goal = "methinks it is like a weasel"
list = generate(len(goal))
print(list)
print(goal)
check(list,goal)
