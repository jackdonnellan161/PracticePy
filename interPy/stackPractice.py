#! /usr/bin/env python3

from pythonds.basic.stack import Stack

word = "Is this backwards?"

def reverseString(mystr):
	a = list(mystr)
	rev = []
	s = Stack()
	for ii in range(len(mystr)):	
		s.push(a.pop())
		rev.append(s.pop())
	return ''.join(rev)

print(reverseString(word))