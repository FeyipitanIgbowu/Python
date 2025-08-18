import unittest
import code_leveling1

class TestTupleModification(unittest.TestCase):
	def test_adding_number(self):
		user_input = code_leveling1.tuple_modification((1, 2, 3, 4, 5), 6)
		self.assertEqual(user_input, (1, 2, 3, 4, 5, 6))
		
	def test_for_invalid_number_type(self):
		self.assertRaises(ValueError, code_leveling1.tuple_modification, 6, (1, 2, 3, 4, 5))
		
	def test_for_negative_value_input(self):
		self.assertRaises(ValueError, code_leveling1.tuple_modification, (1, 2, 3, 4, 5), -8)
	
class TestNumbers(unittest.TestCase):
	def test_for_invalid_input(self):
		self.assertRaises(ValueError, code_leveling1.numbers, 7)
		
	def test_correct_result(self):
		user_input = code_leveling1.numbers((1, 2, [3, 4], 5))
		self.assertEqual(user_input, (1, 2, [3, 99], 5))
			
class TestTupleToListConversion(unittest.TestCase):
	def test_for_invalid_input(self):
		self.assertRaises(ValueError, code_leveling1.string_tuple, 7)
		
	def test_correct_result(self):
		user_input = code_leveling1.string_tuple(('apple', 'banana', 'cherry'))
		self.assertEqual(user_input, ['apple', 'banana', 'cherry', 'mango'])

class TestTupleUnpacking(unittest.TestCase):
	def test_for_invalid_input(self):
		self.assertRaises(ValueError, code_leveling1.tuple_unpacking, 7)
		