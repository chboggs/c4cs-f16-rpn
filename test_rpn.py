import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_multiply(self):
		result = rpn.calculate("5 3 *")
		self.assertEqual(15, result)
	def test_divide(self):
		result = rpn.calculate("20 5 /")
		self.assertEqual(4, result)
	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
	def test_exp(self):
		result = rpn.calculate("5 2 ^")
		self.assertEqual(25, result)
