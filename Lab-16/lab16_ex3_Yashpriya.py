from math import sqrt
#Initialise the perimeter to zero.
perimeter=0
first_x=float(input("Enter the x coordinate"))
first_y=float(input("Enter the y coordinate"))
#Store the values of first x and first y
prev_x=first_x
prev_y=first_y
#Get the x coordinate as input
line=input("Enter the x coordinate: ")
while line!="":
    x=float(line)
    y=float(input("Enter y coordinate: "))
    #Calculate the distance
    distance=sqrt((prev_x-x)**2+(prev_y-y)**2)
    perimeter=distance+perimeter
    #Update previous x and y coordinates
    prev_x = x
    prev_y = y
    #Get the another x coordinate as input
    line=input("Enter the next x coordinate or press 'Enter' to finish the operation")
#Print the output,i.e., the perimeter of a polygon
print("The perimeter of the polygon is", perimeter)