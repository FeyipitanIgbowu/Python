def heat_advisory(temperature, measurement, threshold):
	if temperature == 0 or measurement == 0 or threshold == 0:
		raise ValueError("Invalid Number")
	
	if measurement  == 'C' or measurement == ' ':
		output = (temperature * 9/5) + 32
	elif measurement == 'F':
		output = (temperature - 32) * 5/9
	else:
		raise ValueError("Invalid Input")
	
	if output < threshold:
		return "Cold advisory"
	elif output >= threshold:
		return "Heat Alert"
			
def discount_code(item_name, price, promotional_discount):
	if type(item_name)  !=  " "  and  type(price)  !=  int and type(promotional_discount) != " ":
		raise ValueError("Invalid Type")
	
	if promotional_discount == "SAVE10":
		discount = price - (price * 10 / 100)
	elif promotional_discount == "HALFOFF":
		discount = price - (price * 50 / 100)
	else:
		raise ValueError("Invalid Discount Code")

def palindrome_and_prime(number):
	if number < 2:
		return False

	original = number
	reversed = 0
	
	while number > 0:
		num = number % 10
		reversed = (reversed * 10) + num
		number = number // 10

	if reversed != original:
		return False

	for i in range(2, original):
		 if original % i == 0:
		 	return False
	return True





	
	