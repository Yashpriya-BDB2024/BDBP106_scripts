#Get all the three sides of a triangle from the user as input
side1=float(input("Enter the first side: "))
side2=float(input("Enter the second side: "))
side3=float(input("Enter the third side: "))
#Set default empty string
name=""
#Check if the sides form a valid triangle or not
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
#Check the type of the triangle according to the given sides.
    if side1==side2==side3:
        name="Equilateral triangle"
    elif side1==side2 or side1==side3 or side2==side3:
        name="Isosceles triangle"
    else:
        name="Scalene triangle"
else:
    print('Error')
print(name)
    
