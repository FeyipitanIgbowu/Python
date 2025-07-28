
largest = 0
smallest = 0
collection = []
for number in range(5):
	collection = input("Enter a number: ")
	

if (collection[0] > collection[1] or collection[2] or collection[3] or collection[4]):
	largest = collection[0]
elif (collection[1] > collection[0] or collection[2] or collection[3] or collection[4]):
	largest = collection[1] 
elif (collection[2] > collection[1] or collection[0] or collection[3] or collection[4]):
	largest = collection[2]
elif (collection[3] > collection[1] or collection[2] or collection[0] or collection[4]):
	largest = collection[3]
elif (collection[4] > collection[1] or collection[2] or collection[3] or collection[0]):
	largest = collection[4]
print(largest)

if (collection[0] < collection[1] or collection[2] or collection[3] or collection[4]):
	smallest = collection[0]
elif (collection[1] < collection[0] or collection[2] or collection[3] or collection[4]):
	smallest = collection[1]
elif (collection[2] < collection[1] or collection[0] or collection[3] or collection[4]):
	smallest = collection[2]
elif (collection[3] < collection[1] or collection[2] or collection[0] or collection[4]):
	smallest = collection[3]
elif (collection[4] < collection[1] or collection[2] or collection[3] or collection[0]):
	smallest = collection[4]
print(smallest)

range = largest - smallest
print(range)


