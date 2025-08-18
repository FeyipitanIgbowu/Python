total_miles = 0
total_gallons = 0

for i in range(4):
	miles = int(input("Enter the miles driven ( -1 to end ) : "))
	gallons = int(input("Enter the gallons used ( -1 to end ) : "))

	miles_per_gallon = miles / gallons
	print(miles_per_gallon)
	
	total_miles += miles
	total_gallons += gallons

final_miles_per_gallon = total_miles / total_gallons
print(final_miles_per_gallon)
