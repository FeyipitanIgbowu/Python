import unittest
import array_kata


class TestArrayKata(unittest.TestCase):

    	def test_for_maximum_number(self):
        		result = array_kata.maximumIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 25)

    	def test_for_minimum_number(self):
        		result = array_kata.minimumIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 1)

    	def test_for_sum(self):
        		result = array_kata.sumOf([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 67)

    	def test_for_sum_of_even_numbers(self):
        		result = array_kata.sumOfEvenNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 22)

    	def test_for_sum_of_odd_numbers(self):
        		result = array_kata.sumOfOddNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 45)

    	def test_maximumAndMinimumOf(self):
        		result = array_kata.maximumAndMinimumOf([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, [1, 25])

    	def test_noOfOddNumbersIn(self):
        		result = array_kata.noOfOddNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 5)

    	def test_noOfEvenNumbersIn(self):
        		result = array_kata.noOfEvenNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, 3)

    	def test_evenNumbersIn(self):
        		result = array_kata.evenNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, [2, 4, 16])

    	def test_oddNumbersIn(self):
        		result = array_kata.oddNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, [1, 3, 9, 25, 7])

    	def test_squareNumbersIn(self):
       		 result = array_kata.squareNumbersIn([1, 2, 3, 4, 9, 16, 25, 7])
        		self.assertEqual(result, [1, 4, 9, 16, 25])



