import random
#Write a python program that create a list of 10 random numbers between 1 and 50
new_list = []
for _ in range(50):
	random_num = random.randint(1, 50)
	new_list.append(random_num)
print(new_list)

#Get length of a list without using length function
count = 0
for _ in new_list:
	count += 1
print(count)

#Sum up all the element at even positions
even_count = 0
for num in new_list[0::2]:
	even_count += num
print(even_count)

#Sum up all the elements at odd positions
odd_count = 0
for num in new_list[1::2]:
	odd_count += num
print(odd_count)

#Multiply all element at every third position
third_position = 1
for num in new_list[0::3]:
	third_position *= num
print(third_position)

#calculate the average of all elements in the list
average = 0
for num in new_list[:]:
	average += num
	new_average = average / count
print(new_average)

#Get the largest elements in the list
largest = 0
for num in new_list[:]:
	if num > largest:
		largest = num
print(largest)

#get the smallest elements from the lis
smallest = largest
for num in new_list[:]:
	if num < smallest:
		smallest = num
print(smallest)


words = ["aba", "xyz", "aa", "x", "bbb"]
count = 0   
match = [] 
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
        match.append(word)
print(count)
print(match)


sequential_list = list(range(1, 16))
duplicated_list = []
for num in sequential_list:
    duplicated_list.append(num)
    duplicated_list.append(num)
print(duplicated_list)

new_list = duplicated_list[::2]
print(new_list)


third_element = 0
for num in new_list[2::3]:
	third_element += num
print(third_element)


designated_list = list(range(1, 17))
list_size = len(designated_list)
average = list_size // 2

if list_size % 2 == 0:
	average = designated_list[average - 1 : average + 1]

middle_number = 0
for num in average:
	middle_number += num
median = middle_number / 2

total_sum = designated_list[0] + designated_list[-1] + median
print(total_sum)

#TUPLE
integers = tuple(range(1, 21))

#sum of elements at odd positions
odd_positions = 0
for num in integers[::2]:
	odd_positions += num
print("The sum of odd positions is" , odd_positions)

#sum of elements at even positions
even_positions = 0
for num in integers[1::2]:
	even_positions += num
print("The sum of even positions is" , even_positions)

#sum of the smallest and highest
smallest = 0
for num in integers[:]:
	if num < smallest:
		smallest = num

highest = 0
for num in integers[:]:
	if num > highest:
		highest = num

summation = smallest + highest
print("The sum of the smallest and highest numbers is: ", summation)

#unpacking the first five elements in the tuple
first, second, third, fourth, fifth, *others = integers
print("The first is :" , first)
print("The second is :" , second)
print("The third is :" , third)
print("The fourth is :" , fourth)
print("The fifth is :" , fifth)





