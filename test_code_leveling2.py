import unittest
import code_leveling2

class TestTwoDList(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, code_leveling2.twoD_list_add, 9)
		
	def test_adding_number(self):
		user_input = code_leveling2.twoD_list_add( [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ] ) 
		self.assertEqual(user_input, [9, 13, 18])

	def test_for_zero_input(self):
		self.assertRaises(ValueError, code_leveling2.twoD_list_add, [ [0], [0], [0] ])

	def test_for_zero_input(self):
		self.assertRaises(ValueError, code_leveling2.twoD_list_add, [ [-3], [-2], [-1] ])

class TestSumOfElementsInCorrespondingIndex(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, code_leveling2.element_sum, 9)
		
	def test_adding_number(self):
		user_input = code_leveling2.element_sum( [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ] ) 
		self.assertEqual(user_input, [7, 14, 19])

	def test_for_zero_input(self):
		self.assertRaises(ValueError, code_leveling2.element_sum, [ [0], [0], [0] ])

	def test_for_zero_input(self):
		self.assertRaises(ValueError, code_leveling2.element_sum, [ [-3], [-2], [-1] ])
