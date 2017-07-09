import numpy as np

class RangeFilter:

	def __init__(self, rangeMin , rangeMax):
		self.rangeMin = rangeMin	
		self.rangeMax = rangeMax

	def update(self, lidarData):
		filterData = []

		for index in range(0, len(lidarData)):
			if lidarData[index] <= self.rangeMin:
				lidarData[index] = self.rangeMin
			elif lidarData[index] >= self.rangeMax:
				lidarData[index] = self.rangeMax

		return lidarData
