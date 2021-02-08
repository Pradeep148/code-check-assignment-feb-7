x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
z = int(input("Enter 3rd number : "))
if (x == (y + z)) :
    print("x = y + z")
elif (y == (x + z)) :
    print("y = x + z")
elif (z == (x + y)) :
    print("z = x + y")
else :
    print("None found")
