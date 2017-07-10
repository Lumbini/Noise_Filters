
import unittest
from RangeFilter import RangeFilter


class TestRangeFilter(unittest.TestCase):

	def testInbounds(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([0.05, 0.06, 33, 45, 22]), 
										[0.05, 0.06, 33, 45, 22])
		
	def testEdgeCaseMin(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([0.03, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22]), 
										[0.03, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22])

	def testEdgeCaseMax(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22]), 
										[50, 0.05, 0.23, 0.66, 50, 0.06, 33, 45, 22])

	def testFirstBelow(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([0.003, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22]), 
										[0.03, 0.05, 0.23, 0.66, 0.3, 0.06, 33, 45, 22])

	def testFirstAbove(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([99, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22]), 
										[50, 0.05, 0.23, 0.66, 49, 0.06, 33, 45, 22])

	def testManyBelow(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([0.003, 0.000999, 0.001, 0.66, 0.3, 0.06, 33, 0.00007, 22]), 
										[0.03, 0.03, 0.03, 0.66, 0.3, 0.06, 33, 0.03, 22])

	def testManyAbove(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([99, 82, 33, 90, 500, 0.66, 49, 0.06, 67, 45, 22]), 
										[50, 50, 33, 50, 50, 0.66, 49, 0.06, 50, 45, 22])

	# def testNewRangeBelow(self):
	# 	filter = RangeFilter(0.03, 50)
	# 	self.assertEqual(filter.update([0.003, 0.000999, 0.001, 0.66, 0.3, 0.06, 33, 0.00007, 22]), 
	# 									[0.03, 0.03, 0.03, 0.66, 0.3, 0.06, 33, 0.03, 22])

	# def testNewRangeAbove(self):
	# 	filter = RangeFilter(0, 100)
	# 	self.assertEqual(filter.update([0, 82, 33, 90, 500, 0.66, 49, 0.06, 67, 45, 500, 0.66, 49, -0.06, 67, 500, 0.66, 49, 0.06, 67, 500, 0.66, 49, 0.06, 67, 22]), 
										# [0, 82, 33, 90, 100, 0.66, 49, 0.06, 67, 45, 100, 0.66, 49, 0, 67, 100, 0.66, 49, 0.06, 67, 100, 0.66, 49, 0.06, 67, 22])

	def testEmpty(self):
		filter = RangeFilter(0.03, 50)
		self.assertEqual(filter.update([]),[])




suite = unittest.TestLoader().loadTestsFromTestCase(TestRangeFilter)
unittest.TextTestRunner(verbosity=2).run(suite)