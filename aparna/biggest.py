x=int (input("Enter the digit 1:"))
y=int(input("Enter the digit 2:"))
z=int(input("Enter the digit 3:"))
print(x)
print(y)
print(z)
print("the biggest digit:")
if((x>y)or(x>z)):
    print("x is biggest")
elif(y>z):
    print("y is biggest")
else:
    print("z is biggest")