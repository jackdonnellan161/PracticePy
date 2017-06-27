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
#				print(ii+1)
			ii = ii+1
#	print(count,total)	
	score = count/total
	flag = int(count/total)
	group = [score,flag]
	return group

def looper(most):
	count = 1
	goal = "methinks it is like a weasel"
	generated = generate(len(goal))
	bestString = ''
	bestScore = 0
	end = [bestScore,bestString]
	while check(generated,goal)[1] != 1:
		generated  = generate(len(goal))
		count = count + 1
		if check(generated,goal)[0] > bestScore:
			bestString = generated
			bestScore = check(generated,goal)[0]
			end = [bestScore,bestString]
		if count%100000 == 0:
			print(count,end,sep=": ")
		if count >= most:
			raise RuntimeError("Looping for too long.")
	return end

most = int(input("Maximum number of iterations: "))
looper(most)

