a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))

sum = a + b + c
product = a * b * c

if(a > b  and  a > c): 
 print(a, "Is Largest")
elif ( b > a  and  b > c):
 print(b, "Is Largest")
else:
 print(c , "Is Largest")
 
 
 if(a < b and a < c):
  print(a, "Is Smallest")
 elif ( b < a and b < c):
  print(b, "Is Smallest")
 else:
  print(c, "Is Smallest")