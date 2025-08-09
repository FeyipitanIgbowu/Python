import unittest
import array_kata


class TestArrayKata(unittest.TestCase):

	def test_for_maximum_number(self):
		result = array_kata.maximumIn([1, 2, 3, 4, 9, 16, 25, 7])
		
		self.assertEqual(result, 25)


