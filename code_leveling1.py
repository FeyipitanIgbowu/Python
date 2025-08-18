numbers = (1, 2, 3, 4, 5)
def tuple_modification(numbers, value) :
	if type(numbers) != tuple:
		raise ValueError("Invalid Input")
		
	if value < 0:
		raise ValueError("Invalid Input")
			
	new_numbers = numbers + (value,)
	return new_numbers

result = tuple_modification(numbers, 6)
print(result)


num = (1, 2, [3, 4], 5)	
def numbers(num):
	if type(num) != tuple:
		raise ValueError("Invalid Input")
		
	num[2][1] = 99
	return num
	
num = numbers(num)
print(num)	


string = ('apple', 'banana', 'cherry')
def string_tuple(string):
	if type(string) != tuple:
		raise ValueError("Invalid Input")
	list_conversion = list(string)
	list_conversion.append('mango')
	return list_conversion

final_list = string_tuple(string)
final_tuple = tuple(final_list)
print(final_list)


original_tuple = (10, 20, 30,40)
def tuple_unpacking(original_tuple):
	if type(original_tuple) != tuple:
		raise ValueError("Invalid Input")
	
	a, b, *others = original_tuple
	return a, b, others
	
original_tuple = tuple_unpacking(original_tuple)
print(original_tuple)