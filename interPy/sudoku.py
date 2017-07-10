#! /usr/bin/env python3

#Functions
def imp(fileName):
	#Opens a puzzle from a text file and prints, then confirms
	f = open(fileName,'r')
	puzzle = f.read()
	print(puzzle)
	f.close()
	ans = input("\n Is this the puzzle you want to solve (Y/N)? ")
	if ans == "Y":
		print("Ok")
	else:
		f.close()
		raise RuntimeError("Puzzle not confirmed, please try again.")
	return puzzle.split()

def findPossibles(lines):
	possibles = [[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]],
		[[],[],[],[],[],[],[],[],[]]
		]

	for jj in range(9):
		for kk in range(9):
			column = [r[kk] for r in lines]
			if kk<3:
				if jj<3:
					box = lines[0][0:3]+lines[1][0:3]+lines[2][0:3]
				elif jj<6:
					box = lines[3][0:3]+lines[4][0:3]+lines[5][0:3]
				else:
					box = lines[6][0:3]+lines[7][0:3]+lines[8][0:3]
			elif kk<6:
				if jj<3:
					box = lines[0][3:6]+lines[1][3:6]+lines[2][3:6]
				elif jj<6:
					box = lines[3][3:6]+lines[4][3:6]+lines[5][3:6]
				else:
					box = lines[6][3:6]+lines[7][3:6]+lines[8][3:6]
			else:
				if jj<3:
					box = lines[0][6:]+lines[1][6:]+lines[2][6:]
				elif jj<6:
					box = lines[3][6:]+lines[4][6:]+lines[5][6:]
				else:
					box = lines[6][6:]+lines[7][6:]+lines[8][6:]
			for ii in range (1,10):
				if lines[jj][kk] == "_":
					if str(ii) not in lines[jj] and str(ii) not in column and str(ii) not in box: #Add if not in the same row or column
						possibles[jj][kk].append(ii)
	return possibles

def main():
	#Import board from text file
	puzzle = imp('sudokuPuzzle.txt')

	line = []
	lines = []
	for jj in range(9):
		line = []
		for ii in range(9):
			line.append(puzzle.pop(0))
		lines.append(line)

	# List possibles for each cell
	possibles = findPossibles(lines)
	return possibles

print(main())