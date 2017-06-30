#! /usr/bin/env python3

from pythonds.basic.stack import Stack

def convBase(num,base):
	digits = "0123456789ABCDEF"
	s = Stack()
	ii = 0
	mystr = ''
	if num%1 != 0:
		raise RuntimeError("Integer please")
	if base >16 or base%1 != 0:
		raise RuntimeError("Please chose appropriate base")
	else:
		while num != 0:
			ii = num%base
			s.push(ii)
			num = num//base
	while not s.isEmpty():
			letter = digits[s.pop()]
			mystr = mystr+str(letter)
	return mystr



print(convBase(256,16))