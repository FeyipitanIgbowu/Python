twoD_list = [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]
def twoD_list_add(twoD_list):
	if type(twoD_list) != list:
		raise ValueError("Invalid Input")
		
	for row in twoD_list:
		if any(num <= 0 for num in row):
			raise ValueError("Negative numbers and Zeros are not allowed")
	
	new_list = []	
	for row in twoD_list:
		new_list.append(sum(row))
	return new_list
print(twoD_list_add(twoD_list))


index = [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]	
def element_sum(index):
	if type(index) != list:
		raise ValueError("Invalid Input")
		
	for row in index:
		if any(num <= 0 for num in row):
			raise ValueError("Negative numbers and Zeros are not allowed")

	num_columns = len(index[0])
	new_index = [0] * num_columns
	for row in index:
		for column in range(num_columns):
			new_index[column] += row[column]
	return new_index