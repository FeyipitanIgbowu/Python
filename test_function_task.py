import unittest
import function_task

class TestEvenNumber(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.is_even, "Feyi")

	def test_for_negative_input(self):
		self.assertRaises(ValueError,function_task.is_even, -2)

	def test_for_zero_input(self):
		self.assertRaises(ValueError,function_task.is_even, 0)

	def test_for_correct_result(self):
		user_input = function_task.is_even(2) 
		self.assertEqual(user_input, True)
		
class TestForStringLength(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.is_longer, 7)

	def test_for_correct_result(self):
		user_input = function_task.is_longer(['Rabbits', 'Chickens', 'Dogs']) 
		self.assertEqual(user_input, ['Rabbits', 'Chickens'])
		
class TestForNumbersGreaterThanTwo(unittest.TestCase):
	def test_for_negative_input(self):
		self.assertRaises(ValueError, function_task.greater_than_two, (-2, 'A'))

	def test_for_zero_input(self):
		self.assertRaises(ValueError, function_task.greater_than_two, (0, 'A'))

	def test_for_invalid_data_type_integers(self):
		self.assertRaises(ValueError, function_task.greater_than_two, (7, 6))

	def test_for_invalid_data_type_strings(self):
		self.assertRaises(ValueError, function_task.greater_than_two, ('B', 'A'))
		
		
class TestDivisibilityOfNumbers(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.divisible, "Feyi")

	def test_for_negative_input(self):
		self.assertRaises(ValueError,function_task.divisible, -2)

	def test_for_zero_input(self):
		self.assertRaises(ValueError,function_task.divisible, 0)

	def test_for_correct_result(self):
		user_input = function_task.divisible(25) 
		self.assertEqual(user_input, False)
		

class TestPalindrome(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.palindrome, 7)

	def test_for_correct_result(self):
		user_input = function_task.palindrome('level') 
		self.assertEqual(user_input, True)
		
		
class TestForUpperCaseConvertion(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.convert_uppercase, 7)

	def test_for_correct_result(self):
		user_input = function_task.convert_uppercase(['level', 'feyi'])
		self.assertEqual(user_input, ['LEVEL', 'FEYI'])


class TestSquareOfNumbers(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.square_numbers, "Feyi")

	def test_for_negative_input(self):
		self.assertRaises(ValueError,function_task.square_numbers, -2)

	def test_for_zero_input(self):
		self.assertRaises(ValueError,function_task.square_numbers, 0)

	def test_for_correct_result(self):
		user_input = function_task.square_numbers(5) 
		self.assertEqual(user_input, 25)
		
		
class TestForCapitalizedFirstLetter(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.capitalize, 7)

	def test_for_correct_result(self):
		user_input = function_task.capitalize(['level', 'feyi'])
		self.assertEqual(user_input, ['Level', 'Feyi'])
		

class TestTaxPrices(unittest.TestCase):
	def test_invalid_input_type(self):
		self.assertRaises(ValueError, function_task.tax, "Feyi")

	def test_for_negative_input(self):
		self.assertRaises(ValueError,function_task.tax, -2)

	def test_for_zero_input(self):
		self.assertRaises(ValueError,function_task.tax, 0)

	def test_for_correct_result(self):
		user_input = function_task.tax(100) 
		self.assertEqual(user_input, 110.00000000000001)
		
		
class TestSumOfRangeNumbers(unittest.TestCase):
	def test_correct_result(self):
		result = function_task.sum_of_numbers(range(1, 51))
		self.assertEqual(result, 1275)
	def test_sum_two_numbers(self):
		result = function_task.sum_of_numbers( 2, 3)
		self.assertEqual(result, 5)
		

class TestMaximumNumber(unittest.TestCase):
	def test_correct_result(self):
		result = function_task.maximum_numbers([3, 4, 5])
		self.assertEqual(result, 5)
	

class TestForStringConcatenation(unittest.TestCase):
	def test_for_correct_result(self):
		user_input = function_task.single_string(['Feyi', 'is', 'beautiful'])
		self.assertEqual(user_input, 'Feyi is beautiful')
		
class TestForSquareAndProductOfNumbers(unittest.TestCase):
	def test_correct_result(self):
		result = function_task.maximum_numbers([3, 4,])
		self.assertEqual(result, 4)

		
class TestForStringLength(unittest.TestCase):
	def test_for_negative_input(self):
		self.assertRaises(ValueError, function_task.sum_list_of_tuples, [ (-2, 'A'),  (-2, 'A')])

	def test_for_zero_input(self):
		self.assertRaises(ValueError, function_task.sum_list_of_tuples, [ (0, 0),  (0, 0) ] )

	
class TestForSumOfNumericString(unittest.TestCase):
	def test_for_negative_input(self):
		self.assertRaises(ValueError, function_task.sum_numeric_strings, 5)
	




