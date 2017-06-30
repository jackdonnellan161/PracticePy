#! /usr/bin/env python3

from pythonds.basic.stack import Stack

def postFix(mystr):
	prec = {}
	prec["**"] = 4
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opstack = Stack()
	operator = "+-*/"
	powop = "**"
	parens = "()"
	outList = []
	mystr = mystr.split()
	print(mystr)
	for thing in mystr:
		if thing in operator or thing  == powop:
			if opstack.isEmpty():
				opstack.push(thing)
			else:
				precCurr = prec[thing]
				precOld = prec[opstack.peek()]
				while not opstack.isEmpty() and prec[opstack.peek()]>=prec[thing]:
						outList.append(opstack.pop())
				opstack.push(thing)
		elif thing in parens:
			if thing == parens[0]:
				opstack.push(thing)
			else:
				ii = opstack.pop()
				while ii != "(":
					outList.append(ii)
					ii = opstack.pop()
		else:
			outList.append(thing)
		# print(thing,"Loop ended",sep=": ")
	while not opstack.isEmpty():
		outList.append(opstack.pop())
	return outList

def eval(mystr):
	ops = "+-*/"
	mystr = mystr.split()
	s = Stack()
	for ii in mystr:
		print(ii)
		if ii in ops:
			jj = int(s.pop())
			kk = int(s.pop())
			if ii == "+":
				s.push(jj+kk)
			elif ii == "-":
				s.push(jj-kk)
			elif ii == "*":
				s.push(jj*kk)
			elif ii == "/":
				s.push(kk/jj)
			elif ii == "**":
				s.push(kk**ii)
		else:
			s.push(ii)

	return(s.pop())

print(postFix("5 * 3 ** ( 4 - 2 )"))

