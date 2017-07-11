import numpy as np

class RangeFilter:

	def __init__(self, rangeMin , rangeMax):
		self.rangeMin = rangeMin
		self.rangeMax = rangeMax

	def update(self, lidarData):
		return list(np.clip(lidarData, self.rangeMin, self.rangeMax))

		# ALTERNATE SOLUTION Using Ternary operations:
		# return [self.rangeMin if i < self.rangeMin else self.rangeMax if i > self.rangeMax else i for i in lidarData]
		