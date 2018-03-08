import unittest

import rpn

class TestOperators(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("10 5 -")
		self.assertEqual(5, result)
	def test_multiply(self):
		result = rpn.calculate("7 4 *")
		self.assertEqual(28, result)
	def test_divide(self):
		result = rpn.calculate("60 20 /")
		self.assertEqual(3, result)
	def test_exponate(self):
		result = rpn.calculate("4 3 ^")
		self.assertEqual(64, result)
