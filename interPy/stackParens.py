#! /usr/bin/env python3

from pythonds.basic.stack import Stack

parens1 = "[ [ { { ( ( ) ) } } ] ]"
parens2 = "( [)]"

def parChecker(mystr):
	s = Stack()
	balanced = True
	index = 0
	while index<len(mystr) and balanced:
		a = mystr[index]
		if a == "(" or a == "[" or a == "{":
			s.push(a)
		elif a == " ":
			pass
		else:
			if s.isEmpty():
				balanced = False
			else:
				q = s.pop()
				if a == ")" and q != "(":
					balanced = False
				if a == ")" and q != "(":
					balanced = False
				if a == "}" and q != "{":
					balanced = False
		index = index + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False
print(parChecker(parens1),parChecker(parens2))