#! /usr/bin/env python3

from pythonds.basic.stack import Stack

def convBin(num):
	s = Stack()
	ii = 0
	mystr = ''
	if num%1 != 0:
		raise RuntimeError("Integer please")
	else:
		while num != 0:
			ii = num%2
			s.push(ii)
			num = num//2
	while not s.isEmpty():
		mystr = mystr+str(s.pop())
	return mystr



print(convBin(1000))