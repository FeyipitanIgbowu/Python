first = input("What is your problem")
second = input("Have you had this problem before(Yes or No):")

if second == 'YES' or second == 'Yes' or second == 'yes':
	print("Well, you have it again.")
elif second == 'NO' or second == 'No' or second == 'no':
	print("Well, you have it now.")
else:
	print("Invalid input")