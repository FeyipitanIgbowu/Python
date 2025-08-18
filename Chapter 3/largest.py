largest = 0
second_largest = largest
for num in range(11):
	if num > largest:
		second_largest = largest
		largest = num
	if num != largest and num > second_largest:
		second_largest = num
print(largest)
print(second_largest)