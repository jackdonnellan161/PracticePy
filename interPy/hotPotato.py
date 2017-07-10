#! /usr/bin/env python3

from pythonds.basic.queue import Queue

def hotPotato(names,num):
	q = Queue()
	for ii in names:
		q.enqueue(ii)
	while q.size() != 1:
		for ii in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()
	return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
