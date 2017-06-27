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

def regenerate(number,string):
	#print(number,string)
	possible = "abcdefghijklmnopqrstuvwxyz "
	posList = list(possible)
	newList = list(string)
	kk = randint(0,26)
	#print(newList,number,kk)
	newList[number] = posList[kk]
	regenerated = ''.join(newList)
	return regenerated

def check(generated,goal):
	ii=0
	count = 0
	errorpos = 0
	total = len(generated)
	if len(generated) != len(goal):
		raise RuntimeError("Something went wrong!")
	else:
		while ii<total:
			if generated[ii] == goal[ii]:
				count = count+1
				#print(ii+1)
			else:
				errorPos = ii #Will fix from right to left
				#print(errorPos)
			ii = ii+1
	if count == total:
		return [1,1,0]
	#print(count,total)	
	score = count/total
	flag = int(count/total)
	group = [score,flag,errorPos]
	return group

def looper(most):
	count = 1
	goal = "methinks it is like a weasel"
	generated = generate(len(goal))
	bestString = generated
	bestScore = check(generated,goal)[0]
	end = [bestScore,bestString]
	print(1,end,sep=": ")
	while check(generated,goal)[1] != 1:
		generated  = regenerate(check(generated,goal)[2],bestString)
		#print(generated)
		count = count + 1
		if check(generated,goal)[0] > bestScore:
			bestString = generated
			bestScore = check(generated,goal)[0]
			end = [bestScore,bestString]
		if count%1 == 0:
			print(count,end,sep=": ")
		if count >= most:
			raise RuntimeError("Looping for too long.")
	return end

most = int(input("Maximum number of iterations: "))
looper(most)
