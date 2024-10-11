def cylinder_volume(r, h):
    volume=3.14*(r*r)*h
    volume="%5.2f"%(volume)  #To take the output upto 2 decimal places.
    return volume
def main():
    radius=int(input("Enter the radius of the base of the cylinder: "))
    height=int(input("Enter the height value of the cylinder: "))
    result=cylinder_volume(radius, height)
    print(f"The volume of the cylinder is {result} cubic centimeter.")
if __name__ == "__main__":
    main()