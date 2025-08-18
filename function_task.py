even_numbers = []
def is_even(number):
	if type(number) != int:
		raise ValueError("Invalid Input")
		
	if number < 0 or number == 0:
		raise ValueError("Zeros are not allowed")
	return number % 2 == 0

even_numbers = filter(is_even, range(1, 21))
print(list(even_numbers))


animals = [ 'cat', 'elephant', 'tiger', 'lion' ]
new_animals = []
def is_longer(animals) :
	if type(animals) != list:
		raise ValueError("Invalid Input")
		
	for animal in animals:
		if len(animal) > 5:
			new_animals.append(animal)
	return new_animals


tuple_list = [ (1, 'A'), (4, 'B'), (2, 'C') ]
def greater_than_two(value):
	first_value = value[0]
	second_value = value[1]
	if type(first_value) != int:
		raise ValueError("Invalid Input")
		
	if type(second_value) != str:
		raise ValueError("Invalid Input")
	
	if first_value <= 0:
		raise ValueError("Invalid Input")
		
	return first_value > 2

result = filter(greater_than_two, tuple_list)
print(list(result))


def divisible(number):
	if type(number) != int:
		raise ValueError("Invalid Input")
		
	if number <= 0:
		raise ValueError("Zeros and negative numbers are not allowed")
	return number % 3 == 0 and number % 5 == 0

divisible_number = filter(divisible, range(1, 51))
print(list(divisible_number))


words = ['level', 'world', 'madam', 'python']
def palindrome(word):
	if type(word) != str:
		raise ValueError("Invalid Input")
	return word == word[::-1]
	
new_word = filter(palindrome, words)
print(list(new_word))


words = ['python', 'java', 'c++']
def convert_uppercase(words):
	if type(words) != list:
		raise ValueError("Invalid Input")
	return list(map(str.upper, words))
	
print(convert_uppercase(words))


def square_numbers(number):
	if type(number) != int:
		raise ValueError("Invalid Input")
	
	if number < 0 or number == 0:
		raise ValueError("Zeros and negative numbers are not allowed")
	return number ** 2
	
print(list(map(square_numbers, range(1, 11))))
		
		
names = ['john', 'mary', 'steve']
def capitalize(names):
	if type(names) != list:
		raise ValueError("Invalid Type")
	return list(map(str.capitalize, names))
	
print(list(capitalize(names)))


prices = [100, 200, 300]
def tax(price):
	if type(price) not in (int, float):
		raise ValueError("Invalid Input")
	
	if price <= 0:
		raise ValueError("Zeros and negative numbers are not allowed")
	
	return price * 1.10
	
new_prices = map(tax, prices)
print(list(new_prices))


from functools import reduce
def sum_of_numbers(x, y= None):
	if y is None:
		return reduce(sum_of_numbers, x)
	return x + y
	
result = reduce(sum_of_numbers, range(1, 51))
print(result)


max_num = [3, 5, 9, 2, 8]
def maximum_numbers(x, y= None):
	if y is None:
		return reduce(maximum_numbers, x)
	return x if x > y else y
	
result = reduce(maximum_numbers, max_num)
print(result)


words = ['I', 'Love', 'Python']
def single_string(x, y= None):
	if y is None:
		return reduce(single_string, x)
	return x + " " + y
	
result = reduce(single_string, words)
print(result)
	
	
numbers = [1, 2, 3, 4]
def square(x):
	return x ** 2
def product(a, b = None):
	if b is None:
		return reduce(product, a)
	return a * b

squared = map(square, numbers)
result = reduce(product, squared)
print(result)


list_of_tuples = [ (1, 2), (3, 4), (5, 6) ]
def sum_list_of_tuples(y):
	if type(y) != tuple:
		raise ValueError("Invalid Input")
		
	return sum(y)
def filter_elements(x):
	if type(x) != int:
		raise ValueError("Invalid Input")
	return x > 5
	
sums = map(sum_list_of_tuples, list_of_tuples)
result = filter(filter_elements, sums)
print(list(result))
	

data = [ '123', '456', '789', 'abc', 'def' ]
def sum_numeric_strings(data):
	if type(data) != list:
		raise ValueError("Invalid Input")
	numbers = 0
	for item in data:
		if item.isdigit():
			numbers += int(item)
	return numbers
print(sum_numeric_strings(data))
	
