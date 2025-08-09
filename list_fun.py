import random
new_list = []
for _ in range(50):
	random_num = random.randint(1, 50)
	new_list.append(random_num)
print(new_list)

count = 0
for _ in new_list:
	count += 1
print(count)

even_count = 0
for num in new_list[0::2]:
	even_count += num
print(even_count)

odd_count = 0
for num in new_list[1::2]:
	odd_count += num
print(odd_count)

third_position = 1
for num in new_list[0::3]:
	third_position *= num
print(third_position)

average = 0
for num in new_list[:]:
	average += num
	new_average = average / count
print(new_average)

largest = 0
for num in new_list[:]:
	if num > largest:
		largest = num
print(largest)

smallest = largest
for num in new_list[:]:
	if num < smallest:
		smallest = num
print(smallest)
