#!/usr/bin/python

import sys

#python programa.py 3 3 -1,0,-1,0,0,-1,-1,-1,-1 0,1 -v
#python programa.py 3 3 -1,0,-1,-1,0,-1,-1,0,-1 0,1 -v
#python programa.py 4 4 -1,0,-1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,0,-1,-1 0,1 -v

def main(argv):
	row = int(sys.argv[1])
	column = int(sys.argv[2])
	lab = sys.argv[3].split(",")
	start = [int(x) for x in sys.argv[4].split(",")]
	labmap = [[0 for x in range(row)] for y in range(column)]
	
	verbose = False
	
	if (sys.argv[len(sys.argv)-1] == "-v"):
		verbose = True

	if verbose: print 'starter labirynth'
	for i in range(0, row):
		for j in range(0, column):
			labmap[i][j] = int(lab[i*row+j])
			if verbose: print labmap[i][j],
		if verbose: print ''
	if verbose: print '---'
	
	coord = start
	path = []
	path.append(coord)
	if verbose:
		print 'path inicial', path
		print 'coord inicial', coord
	checking = True
	mappath = labmap
	bifu = []

	if (mappath[coord[0]][coord[1]] == 0):
		mappath[coord[0]][coord[1]] = 1
	else:
		checking = False
	
	while checking:
		if (coord[0]-1 >= 0) and (mappath[coord[0]-1][coord[1]] == 0): #check upper
			path.append([coord[0]-1,coord[1]])
			mappath[coord[0]-1][coord[1]] = 1
			coord = [coord[0]-1,coord[1]]
		elif (coord[1]+1 < column) and (mappath[coord[0]][coord[1]+1] == 0): #check right
			path.append([coord[0],coord[1]+1])
			mappath[coord[0]][coord[1]+1] = 1
			coord = [coord[0],coord[1]+1]
		elif (coord[0]+1 < row) and (mappath[coord[0]+1][coord[1]] == 0): #check bottom
			path.append([coord[0]+1,coord[1]])
			mappath[coord[0]+1][coord[1]] = 1
			coord = [coord[0]+1,coord[1]]
		elif (coord[1]-1 >= 0) and (mappath[coord[0]][coord[1]-1] == 0): #check left
			path.append([coord[0],coord[1]-1])
			mappath[coord[0]][coord[1]-1] = 1
			coord = [coord[0],coord[1]-1]
		else:
			#print 'else'
			checking = False
	
	if verbose:
		print 'path', path
	
	print 'final labirynth'
	for i in range(0, row):
		for j in range(0, column):
			print mappath[i][j],
		print ''

if __name__ == "__main__":
	main(sys.argv[1:])