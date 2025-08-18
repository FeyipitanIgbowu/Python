x = 42
y = 12
z = 55

second_highest = 1

if  x > y < z:
 second_highest = x
elif x > z < y:
 second_highest = x
elif y > z < x:
 second_highest = y
elif y > x < z:
 second_highest = y
elif z > x < y:
 second_highest = z
elif z > y < x:
 second_highest = z
 
print(second_highest) 
 

