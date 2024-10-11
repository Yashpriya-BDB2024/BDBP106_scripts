import math
def right_triangle_hypotenuse(P, B):
    hypotenuse=((B*B)+(P*P))**0.5
    hypotenuse="%5.2f" % (hypotenuse) #To take the output upto 2 decimal places.
    return hypotenuse
def main():
    perpendicular=int(input("Enter the length of perpendicular: "))
    base=int(input("Enter the length of base of the right angled triangle: "))
    result=right_triangle_hypotenuse(perpendicular, base)
    print(f"The length of the hypotenuse of right angled triangle is {result} cm")
if __name__ == "__main__":
    main()
