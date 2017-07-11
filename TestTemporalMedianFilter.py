
import unittest
from TemporalMedianFilter import TemporalMedianFilter

class TestTemporalMedianFilter(unittest.TestCase):

	def testFirstScan(self):
		filter = TemporalMedianFilter(1)
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		self.assertEqual(filter.update(input1), input1)

	def testFirstTwoScans(self):
		filter = TemporalMedianFilter(3)
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		self.assertEqual(filter.update(input1), expected1)
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		self.assertEqual(filter.update(input2), expected2)

	def testFirstThreeScans(self):
	    filter = TemporalMedianFilter(3)
	    input1 = [0., 1., 2., 1., 3.]
	    expected1 = [0., 1., 2., 1., 3.]
	    self.assertEqual(filter.update(input1), expected1)
	    input2 = [1., 5., 7., 1., 3.]
	    expected2 = [0.5, 3., 4.5, 1., 3.]
	    self.assertEqual(filter.update(input2), expected2)
	    input3 = [2., 3., 4., 1., 0.]
	    expected3 = [1., 3., 4., 1., 3.]
	    self.assertEqual(filter.update(input3), expected3)

	def testFirstFourScans(self):
	    filter = TemporalMedianFilter(3)
	    input1 = [0., 1., 2., 1., 3.]
	    expected1 = [0., 1., 2., 1., 3.]
	    self.assertEqual(filter.update(input1), expected1)
	    input2 = [1., 5., 7., 1., 3.]
	    expected2 = [0.5, 3., 4.5, 1., 3.]
	    self.assertEqual(filter.update(input2), expected2)
	    input3 = [2., 3., 4., 1., 0.]
	    expected3 = [1., 3., 4., 1., 3.]
	    self.assertEqual(filter.update(input3), expected3)
	    input4 = [3., 3., 3., 1., 3.]
	    expected4 = [1.5, 3., 3.5, 1., 3.]
	    self.assertEqual(filter.update(input4), expected4)

	# note that this is the point at which the first scan starts to be ignored by the temporal filte
	def testFirstFiveScans(self):
	    filter = TemporalMedianFilter(3)
	    input1 = [0., 1., 2., 1., 3.]
	    expected1 = [0., 1., 2., 1., 3.]
	    self.assertEqual(filter.update(input1), expected1)
	    input2 = [1., 5., 7., 1., 3.]
	    expected2 = [0.5, 3., 4.5, 1., 3.]
	    self.assertEqual(filter.update(input2), expected2)
	    input3 = [2., 3., 4., 1., 0.]
	    expected3 = [1., 3., 4., 1., 3.]
	    self.assertEqual(filter.update(input3), expected3)
	    input4 = [3., 3., 3., 1., 3.]
	    expected4 = [1.5, 3., 3.5, 1., 3.]
	    self.assertEqual(filter.update(input4), expected4)
	    input5 = [10., 2., 4., 0., 0.]
	    expected5 = [2.5, 3., 4., 1., 1.5]
	    self.assertEqual(filter.update(input5), expected5)

	def testSixScans(self):
		filter = TemporalMedianFilter(3)
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		self.assertEqual(filter.update(input1), expected1)
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		self.assertEqual(filter.update(input2), expected2)
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		self.assertEqual(filter.update(input3), expected3)
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [1.5, 3., 3.5, 1., 3.]
		self.assertEqual(filter.update(input4), expected4)
		input5 = [10., 2., 4., 0., 0.]
		expected5 = [2.5, 3., 4., 1., 1.5]
		self.assertEqual(filter.update(input5), expected5)
		input6 = [21., 3., 1., 7., 4.]
		expected6 = [6.5, 3., 3.5, 1., 1.5]
		self.assertEqual(filter.update(input6), expected6)


	def testFiveScansWithDifferenceD(self):
		filter = TemporalMedianFilter(2)
		input1 = [0., 1., 2., 1., 3.]
		expected1 = [0., 1., 2., 1., 3.]
		self.assertEqual(filter.update(input1), expected1)
		input2 = [1., 5., 7., 1., 3.]
		expected2 = [0.5, 3., 4.5, 1., 3.]
		self.assertEqual(filter.update(input2), expected2)
		input3 = [2., 3., 4., 1., 0.]
		expected3 = [1., 3., 4., 1., 3.]
		self.assertEqual(filter.update(input3), expected3)
		input4 = [3., 3., 3., 1., 3.]
		expected4 = [2., 3., 4., 1., 3.]
		self.assertEqual(filter.update(input4), expected4)
		input5 = [10., 2., 4., 0., 0.]
		expected5 = [3., 3., 4., 1., 0.]
		self.assertEqual(filter.update(input5), expected5)

# Runs tests and displays the details of the results
suite = unittest.TestLoader().loadTestsFromTestCase(TestTemporalMedianFilter)
unittest.TextTestRunner(verbosity=2).run(suite)