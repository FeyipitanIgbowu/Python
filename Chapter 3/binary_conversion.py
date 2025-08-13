binary = int(input("Enter a binary number: "))
decimal = 0
position = 0

while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** position)
    binary //= 10
    position += 1

print("Decimal value:", decimal)
