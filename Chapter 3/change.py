
price = float(input("Enter the item's price: "))
change = int(round((1.00 - price) * 100))

quarters = change // 25
change %= 25
dimes = change // 10
change %= 10
nickels = change // 5
change %= 5
pennies = change

print("Your change is:" quaters, dimes, nickels, pennies)
