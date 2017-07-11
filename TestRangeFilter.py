
import unittest
from RangeFilter import RangeFilter


class TestRangeFilter(unittest.TestCase):

	def testEmpty(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([]),[])

	def testInbounds(self):
		filter = RangeFilter(0.03, 50)
		input = 	[0.05, 0.06, 33, 45, 22]
		expected = 	[0.05, 0.06, 33, 45, 22]
		self.assertEqual(filter.update(input), expected)
		
	def testEdgeCaseMin(self):
		filter = RangeFilter(0.03, 50)
		input = 	[0.03, 0.05, 0.23, 0.66, 0.03, 0.06, 33, 45, 22]
		expected = 	[0.03, 0.05, 0.23, 0.66, 0.03, 0.06, 33, 45, 22]
		self.assertEqual(filter.update(input),expected)

	def testEdgeCaseMax(self):
		filter = RangeFilter(0.03, 50)
		input = 	[50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22]
		expected = 	[50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22]
		self.assertEqual(filter.update(input), expected)

	def testFirstBelow(self):
		filter = RangeFilter(0.03, 50)
		input = 	[0.003, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22]
		expected = 	[0.03, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22]
		self.assertEqual(filter.update(input), expected)

	def testFirstAbove(self):
		filter = RangeFilter(0.03, 50)
		input = [99, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22]
		expected = [50, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22]
		self.assertEqual(filter.update(input), expected) 
										
	def testManyBelow(self):
		filter = RangeFilter(0.03, 50)
		input = 	[0.003, 0.000999, 0.001, 0.66, 0.3, 0.06, 33, 0.00007, 22]
		expected = 	[0.03, 0.03, 0.03, 0.66, 0.3, 0.06, 33, 0.03, 22]
		self.assertEqual(filter.update(input), expected)

	def testManyAbove(self):
		filter = RangeFilter(0.03, 50)
		input = 	[99, 82, 33, 90, 500, 0.66, 49, 0.06, 67, 45, 22]
		expected = 	[50, 50, 33, 50, 50, 0.66, 49, 0.06, 50, 45, 22]
		self.assertEqual(filter.update(input), expected)

	def testBothRanges(self):
		filter = RangeFilter(0.03, 50)
		input = 	[99, 82, 33, 0.0093, 90, 500, 0.029, 0.12, 699, 0.66, 49, 0.06, 67, 45, 22, 0.03, 50]
		expected = 	[50, 50, 33, 0.03, 50, 50, 0.03, 0.12, 50, 0.66, 49, 0.06, 50, 45, 22, 0.03, 50]
		self.assertEqual(filter.update(input), expected)

	def testNegative(self):
		filter = RangeFilter(0.03, 50)
		input = 	[99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22]
		expected = 	[50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22]
		self.assertEqual(filter.update(input), expected)
	
	def testDifferentRanges(self):
		filter = RangeFilter(1, 100)
		input = 	[99, 82, 33, 0.0093, 90, 500, 0.029, 0.12, 699, 0.66, 49, 0.06, 67, 45, 22]
		expected = 	[99, 82, 33, 1, 90, 100, 1, 1, 100, 1, 49, 1, 67, 45, 22]
		self.assertEqual(filter.update(input), expected)

	def testNegativeRanges(self):
		filter = RangeFilter(-32, 33)
		input = 	[99, 82, 33, -0.0093, 90, -500, 0.029, 0.12, 699, 0.66, -49, 0.06, 67, 45, 22]
		expected = 	[33, 33, 33, -0.0093, 33, -32, 0.029, 0.12, 33, 0.66, -32, 0.06, 33, 33, 22]
		self.assertEqual(filter.update(input), expected)

	def testLargeScan(self):
		filter = RangeFilter(0.03, 50)
		input = 	[99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22, 99, 82, -33, 0.0093, 90, 500, 0.029, 0.12, -699, 0.66, 49, -0.06, 67, 45, 22]
		expected = 	[50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, 50, 50, 0.03, 0.03, 50, 50, 0.03, 0.12, 0.03, 0.66, 49, 0.03, 50, 45, 22, ]
		self.assertEqual(filter.update(input), expected)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRangeFilter)
unittest.TextTestRunner(verbosity=2).run(suite)