largest = 0
second_largest = 0

for i in range(10):
	num = int(input("Enter a number: ")
	if num > largest:
		second_largest = largest
		largest = num
	elif num > second_largest:
		second_largest = num
print(largest)
print(second_largest)