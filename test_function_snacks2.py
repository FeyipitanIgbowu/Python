import unittest
import function_snacks2

class TestHeatAdvisory(unittest.TestCase):
	
	def test_for_zero_input(self):
		self.assertRaises(ValueError,function_snacks2.heat_advisory, 0, 0, 0)

	def test_default_unit_is_celsius(self):
		output = function_snacks2.heat_advisory(30, ' ', threshold=100)
		self.assertEqual(output, "Cold advisory")
	
	def test_invalid_input(self):
		self.assertRaises(ValueError, function_snacks2.heat_advisory, 100, 'K', 100)
            
	def test_celsius_to_fahrenheit_above_threshold(self):
		threshold = function_snacks2.heat_advisory(30, 'C', 100)
		self.assertEqual(threshold, "Cold advisory")
    
	def test_celsius_to_fahrenheit_below_threshold(self):
		threshold = function_snacks2.heat_advisory(20, 'C', 50)
		self.assertEqual(threshold, "Heat Alert")
		
	def test_fahrenheit_to_celsius_above_threshold(self):
		threshold =  function_snacks2.heat_advisory(104, 'F', 100)
		self.assertEqual(threshold, "Cold advisory")
		
	def test_fahrenheit_to_celsius_below_threshold(self):
		threshold =  function_snacks2.heat_advisory(50, 'F', 50)
		self.assertEqual(threshold, "Cold advisory")
		

class TestDiscountCode(unittest.TestCase):

	def test_for_incomplete_input(self):
		self.assertRaises(ValueError, function_snacks2.discount_code,"Cerelac", ' ', "HALFOFF")
		
	def test_for_incorrect_input_position(self):
		self.assertRaises(ValueError, function_snacks2.discount_code , 100,  "Cerelac", 10)

	def test_10_percent_promotional_discount(self):
		discount = function_snacks2.discount_code("Cerelac", 100, "SAVE10")
		
	def test_50_percent_promotional_discount(self):
		discount = function_snacks2.discount_code("Cerelac", 100, "HALFOFF")

	def test_invalid_percent_promotional_discount(self):
		self.assertRaises(ValueError, function_snacks2.discount_code, "Cerelac", 100, "Feyi")

class TestPalindromePrime(unittest.TestCase):
	def test_that_number_is_palindrome_and_prime(self):
		self.assertTrue(palindrome_and_prime(2))
		self.assertTrue(palindrome_and_prime(11))
		self.assertTrue(palindrome_and_prime(131))

	def test_that_number_is_not_prime_or_palindrome(self):
		self.assertFalse(palindrome_and_prime(121)) 
		self.assertFalse(palindrome_and_prime(13))   
		self.assertFalse(palindrome_and_prime(0))    
		self.assertFalse(palindrome_and_prime(1))    


	