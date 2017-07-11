#!/usr/bin/env python

import numpy as np

class RangeFilter:

	def __init__(self, rangeMin , rangeMax):
		""" Constructor """
		self.rangeMin = rangeMin
		self.rangeMax = rangeMax

	def update(self, lidarData):
		""" Receives raw scan and eliminates the outliers in the data 
		and replaces them with the min and max specified ranges """

		# Uses numpy's clip(array, min, max) function to create a range filter
		return list(np.clip(lidarData, self.rangeMin, self.rangeMax))

		# ALTERNATE SOLUTION Using Ternary operations without numpy:
		# return [self.rangeMin if i < self.rangeMin else self.rangeMax if i > self.rangeMax else i for i in lidarData]

		# ALTERNATE SOLUTION without ternary operations and numpy:
		# for index in range(0, len(lidarData)):
		# 	if lidarData[index] <= self.rangeMin:
		# 		lidarData[index] = self.rangeMin
		# 	elif lidarData[index] >= self.rangeMax:
		# 		lidarData[index] = self.rangeMax
		# return lidarData
