age = int(input("Input your age: "))

maximum_heart_rate = 220 - age 
print("Your maximum heart rate is: ", maximum_heart_rate)

lower_bound = 0.5 * maximum_heart_rate
upper_bound = 0.85 * maximum_heart_rate
print("Your target heart rate is between", lower_bound, "and",upper_bound) 