money = int(input("Enter the amount: "))
amount = 1000 - money
quaters = amount // 25
dimes = amount //  50
pennies = amount // 100
print("Your change is " ,quaters ,"quaters", dimes ,"dimes and", pennies ,"pennies")