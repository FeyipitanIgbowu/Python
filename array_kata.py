def maximumIn(number):
	max_value = number[0]
	for num in number:
		if num > max_value:
			max_value = num		
	return max_value

def minimumIn(number):
	min_value = number[0]
	for num in number:
		if num < min_value:
			min_value = num
		return min_value

def sumOf(number):
	total = 0
	for num in number:
		total += num
	return total

def sumOfEvenNumbersIn(number):
	total = 0
	for num in number:
		if num % 2 == 0:
			total += num
		return total

def sumOfOddNumbersIn(number):
	total = 0
	for num in number:
		if num % 2 != 0:
			total += num
		return total

def maximumAndMinimumOf(number):
	min_value = number[0]
	max_value = number[0]
	for num in number:
		if num < min_value:
			min_value = num
		if num > max_value:
			max_value = num
		return [min_value, max_value]
	
def noOfOddNumbersIn(number):
	count = 0
	for num in number:
		if num % 2 != 0:
			count += 1
		return count

def noOfEvenNumbersIn(number):
	count = 0
	for num in number:
		if num % 2 == 0:
			count += 1
		return count

def evenNumbersIn(number):
	result = []
	for num in number:
		if num % 2 == 0:
			result.append(num)
		return result

def oddNumbersIn(number):
	result = []
	for num in number:
		if num % 2 != 0:
			result.append(num)
		return result

def squareNumbersIn(number):
	result = []
	for num in number:
		i = 1
	while i * i <= num:
		if i * i == num:
			result.append(num)
		break
		i += 1
	return result

