import sys
import trees

dataset = []

def readtxt(file):
	fr = open(file)
	for line in fr.readlines():
		lines = line.strip().split('\t')
		dataset.append(lines)


if __name__ == '__main__':
	readtxt("testSet.txt")
	print trees.choosetosplit(dataset)	
