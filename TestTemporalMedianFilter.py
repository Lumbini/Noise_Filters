
#!/usr/bin/env python

import unittest
from TemporalMedianFilter import TemporalMedianFilter

class TestTemporalMedianFilter(unittest.TestCase):

	# Helper Function
	# Help set up the test, can be repeated several time swith addiontional inputs
	def helpSetUp(self, D, input1, expected1, *therest):
		filter = TemporalMedianFilter(D)
		self.assertEqual(filter.update(input1), expected1)

	# Test with D=3, 1st scan only
	def testFirstScan(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		self.helpSetUp(3, input1, expected1)

	# Test with D=3, First 2 scans
	def testFirstTwoScans(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		self.helpSetUp(3, input1, expected1, input2, expected2)

	# Test with D=3, First 3 scans
	def testFirstThreeScans(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		self.helpSetUp(3, input1, expected1, input2, expected2, input3, expected3)

	# Test with D=3, First 4 scans
	def testFirstFourScans(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [1.5, 3., 3.5, 1., 3.]
		self.helpSetUp(3, input1, expected1, input2, expected2, input3, expected3, input4, expected4)

	# Test with D=3, First 5 scans
	# note that this is the point at which the first scan gets ignored by the temporal median filter
	def testFirstFiveScans(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [1.5, 3., 3.5, 1., 3.]
		input5 = [10., 2., 4., 0., 0.]
		expected5 = [2.5, 3., 4., 1., 1.5]
		self.helpSetUp(3, input1, expected1, input2, expected2, input3, expected3, input4, expected4, input5, expected5)

	# Test with D=3, First 6 scans
	# note that this is the point at which the first 2 scans gets ignored by the temporal median filter
	def testSixScans(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [1.5, 3., 3.5, 1., 3.]
		input5 = [10., 2., 4., 0., 0.]
		expected5 = [2.5, 3., 4., 1., 1.5]
		input6 = [21., 3., 1., 7., 4.]
		expected6 = [6.5, 3., 3.5, 1., 1.5]
		self.helpSetUp(2, input1, expected1, input2, expected2, input3, expected3, input4, expected4, input5, expected5, input6, expected6)

	# Test with D=2, First 5 scans
	# The first 2 scans get ignored by the temporal median filter
	def testFiveScansWithDifferenceD(self):
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [2., 3., 4., 1., 3.]
		input5 = [10., 2., 4., 0., 0.]
		expected5 = [3., 3., 4., 1., 0.]
		self.helpSetUp(3, input1, expected1, input2, expected2, input3, expected3, input4, expected4, input5, expected5)

# Runs tests and displays the details of the results
suite = unittest.TestLoader().loadTestsFromTestCase(TestTemporalMedianFilter)
unittest.TextTestRunner(verbosity=2).run(suite)