#!/usr/bin/env python

import numpy as np

class TemporalMedianFilter:

	def __init__(self, D):
		""" Constructor """
		self.D = D
		self.prevData = []
		# This counter is used to keep track of the number of scans
		# passed into the filter
		self.counter = 0

	def savePrevData(self, lidarData):
		""" Maintains the specified D number of previous 
		scans in the prevData array. """

		# Check is the saved scans is greater or equal
		# to the specified D value. 
		if len(self.prevData) <= self.D:
			self.prevData.append(lidarData)
			self.counter += 1

		# If the number of stored prev scans is greater 
		# than D the modulo function is used to replace 
		# the oldest scan with the latest previous scan
		else:
			insertInto = (self.counter-1) % self.D
			self.prevData[insertInto] = lidarData
			self.counter += 1

	def calculateMedian(self, lidarData):
		""" Calculates the median of individual scans at
			the saved number of scans """

		# Resulting data after passed through Temporal 
		# Median Filter
		medianOfData = []

		# For loop to iterate though each scan 
		for x in range(0, len(lidarData)):
			# Temporary array to calculate median of the set
			tempArrForMedian = []
			# For loop to iterate through the stored previous scans
			for y in self.prevData:
				tempArrForMedian.append(y[x])
			# Calculated the median of all first, second, third... values
			medianOfData.append(np.median(tempArrForMedian))
		return medianOfData

	def update(self, lidarData):
		""" Receives the latest raw scan and passes it into the 
		Temporal median filter and returns the resulting data """
		self.savePrevData(lidarData)
		return self.calculateMedian(lidarData)
		