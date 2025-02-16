#Get the number as input
number=int(input("Enter the number: "))
#Check whether this number is divisible by 3 or not
if number==0:
    print("Zero is not divisible by 3")
elif number%3==0:
    print("The given number is divisible by 3")
else:
    print("The given number is not divisible by 3")
