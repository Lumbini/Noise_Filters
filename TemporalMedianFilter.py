import numpy as np

class TemporalMedianFilter:

	def __init__(self, D):
		self.D = D
		self.prevData = []
		self.counter = 0

	def update(self, lidarData):
		if len(self.prevData) <= self.D:
			self.prevData.append(lidarData)
			self.counter += 1
		else:
			insertInto = (self.counter-1) % self.D
			self.prevData[insertInto] = lidarData
			self.counter += 1

		medianOfData = []
		
		for x in range(0, len(lidarData)):
			tempForMedian = []
			for y in self.prevData:
				tempForMedian.append(y[x])
			medianOfData.append(np.median(tempForMedian))
		return medianOfData		