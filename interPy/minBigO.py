#! /usr/bin/env python3

import time

def minOn(list1):
	i = time.time()
	mini = list1[0]
	for ii in list1:
		if ii<mini:
			mini = ii
	j = time.time()
	return mini,j-i

def minO2n(list1):
	i = time.time()
	mini = list1[0]
	for ii in list1:
		for kk in list1:
			if ii >= kk and kk<mini:
				mini = kk
			elif ii <= kk and ii<mini:
				mini = ii
	j = time.time()
	return mini,j-i

def main():
	n = 10000
	for ii in range(5):
		print("{:d}: Min is {:d} and minOn took {:.7f} seconds to run"\
			.format(n,*minOn([0,10,11,20,1,-10,2,1,0])))
		print("{:d}: Min is {:d} and minO2n took {:.7f} seconds to run\n"\
			.format(n,*minO2n([0,10,11,20,1,-10,2,1,0])))

main()