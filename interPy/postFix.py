#! /usr/bin/env python3

from pythonds.basic.stack import Stack

def postFix(mystr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opstack = Stack()
	operator = "+-*/"
	parens = "()"
	outList = []
	mystr = mystr.split()
	print("".join(mystr))
	for thing in mystr:
		if thing in operator:
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
	return "".join(outList)

print(postFix("A * B + C * D"))
print(postFix("( A + B ) * C - ( D - E ) * ( F + G )"))