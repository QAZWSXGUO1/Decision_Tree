from math import log
#from numpy import np

def calcshannonEnt(dataSet):
	"""
		cal Ent
	"""
	num = len(dataSet)
	label = {}
	for feat in dataSet:
		currentlabel = feat[-1]
		if currentlabel not in label:
			label[currentlabel] = 0
		label[currentlabel] += 1
	shannonEnt = 0.0
	for i in label:
		prob = float(label[i])	 / num
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt



def splitdataset(dataSet, axis, value):
	ret = []
	for feat in dataSet:
		if feat[axis] == value:
			reducedfeat = feat[:axis]
			reducedfeat.extend(feat[axis + 1:])
			ret.append(reducedfeat)
	return ret

def choosetosplit(dataSet):
	featnum = len(dataSet[0]) - 1
	baseEnt = calcshannonEnt(dataSet)	
	bestGain = 0.0
	bestFeat = -1
	for i in range(featnum):
		featList = [ex[i] for ex in dataSet]
		uniqVals = set(featList)
		newEnt = 0.0
		for value in uniqVals:
			subDataSet = splitdataset(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEnt += prob * calcshannonEnt(subDataSet)
		infoGain = baseEnt - newEnt
		if(infoGain > bestGain):
			bestGain = infoGain
			bestFeat = 1

	return bestFeat
