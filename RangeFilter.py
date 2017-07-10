import numpy as np

class RangeFilter:

	def __init__(self, rangeMin , rangeMax):
		self.rangeMin = rangeMin	
		self.rangeMax = rangeMax

	def update(self, lidarData):
		return list(np.clip(lidarData, self.rangeMin, self.rangeMax))