#To determine the name of a shape from its number of sides.
#Get the number of sides as input
no_of_sides=int(input("Enter the sides: "))
#Set the default empty string
name=""
#print the appropriate message as per following conditions -
if no_of_sides==3:
    name="Triangle"
elif no_of_sides==4:
    name="Quadrilateral"
elif no_of_sides==5:
    name="Pentagon"
elif no_of_sides==6:
    name="Hexagon"
elif no_of_sides==7:
    name="Heptagon"
elif no_of_sides==8:
    name="Octagon"
elif no_of_sides==9:
    name="Nonagon"
elif no_of_sides==10:
    name="Decagon"
else:
    print('Error')
#Print the name of the shapes
print(name)
    
