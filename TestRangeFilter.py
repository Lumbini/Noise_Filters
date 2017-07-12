
#!/usr/bin/env python

import unittest
from RangeFilter import RangeFilter

class TestRangeFilter(unittest.TestCase):

	# Helper function, sets up the test with given ranges and inout and expected output
	def helpSetUp(self, min, max, input, output):
		filter = RangeFilter(min, max)
		self.assertEqual(filter.update(input),output)

	# Test to ensure empty arrays dont crash the program
	def testEmpty(self):
		self.helpSetUp(0.03, 50, [], [])

	# Testing all values inside the range
	def testInbounds(self):
		self.helpSetUp(0.03, 50, [0.05, 0.06, 33, 45, 22], 
								 [0.05, 0.06, 33, 45, 22])
		
	# Testing values equal to min range
	def testEdgeCaseMin(self):
		self.helpSetUp(0.03, 50, [0.03, 0.05, 0.23, 0.66, 0.03, 0.06, 33, 45, 22], 
								 [0.03, 0.05, 0.23, 0.66, 0.03, 0.06, 33, 45, 22])

	# Testing values equal to max range
	def testEdgeCaseMax(self):
		self.helpSetUp(0.03, 50, [50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22], 
								 [50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22])

	# Testing one value below range
	def testFirstBelow(self):
		self.helpSetUp(0.03, 50, [0.003, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22], 
								 [0.03, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22])

	# Testing one value above range
	def testFirstAbove(self):
		self.helpSetUp(0.03, 50, [99, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22], 
								 [50, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22])
	
	# Testing many values below range	
	def testManyBelow(self):
		self.helpSetUp(0.03, 50, [99, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22], 
								 [50, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22])
	
	# Testing many values above range
	def testManyAbove(self):
		self.helpSetUp(0.03, 50, [99, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22], 
								 [50, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22])

	# Testing both min and max out of bounds
	def testBothRanges(self):
		self.helpSetUp(0.03, 50, [99, 82, 33, 0.0093, 90, 500, 0.029, 0.12, 699, 0.66, 49, 0.06, 67, 45, 22, 0.03, 50], 
								 [50, 50, 33, 0.03, 50, 50, 0.03, 0.12, 50, 0.66, 49, 0.06, 50, 45, 22, 0.03, 50])

	# Testing negative values in scans
	def testNegative(self):
		self.helpSetUp(0.03, 50, [99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22], 
								 [50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22])
	
	# Testing different ranges 
	def testDifferentRanges(self):
		self.helpSetUp(1, 100, [99, 82, 33, 0.0093, 90, 500, 0.029, 0.12, 699, 0.66, 49, 0.06, 67, 45, 22], 
								 [99, 82, 33, 1, 90, 100, 1, 1, 100, 1, 49, 1, 67, 45, 22])
	
	# Testing negative ranges 
	def testNegativeRanges(self):
		self.helpSetUp(-32, 33, [99, 82, 33, -0.0093, 90, -500, 0.029, 0.12, 699, 0.66, -49, 0.06, 67, 45, 22], 
								 [33, 33, 33, -0.0093, 33, -32, 0.029, 0.12, 33, 0.66, -32, 0.06, 33, 33, 22])
	
	# Testing a large scan of 150 values
	def testLargeScan(self):
		self.helpSetUp(0.03, 50, [99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22], 
								 [50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22])

# Runs tests and displays the details of the results
suite = unittest.TestLoader().loadTestsFromTestCase(TestRangeFilter)
unittest.TextTestRunner(verbosity=2).run(suite)