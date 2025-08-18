passes = 0
failure = 0

for student in range(10):
	result = int(input("Enter result (1 = pass, 2 = fail): "))
	while True:
		if result == 1:
			passes = passes + 1
			break
		elif result == 2:
			failure = failure + 1
			break
		else:
			result = int(input("Enter result (1 = pass, 2 = fail): "))
		
print("Passed:", passes)
print("failed:", failure)

if passes > 8:
	print("Bonus to instructor")