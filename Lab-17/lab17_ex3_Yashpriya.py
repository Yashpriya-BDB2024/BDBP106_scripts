def get_ordinal(num):
#convert the input to an integer
    num=int(num)
#Return the ordinal no. for the given integer
    if num == 1:
        return "first"
    elif num == 2:
        return "second"
    elif num == 3:
        return "third"
    elif num == 4:
        return "fourth"
    elif num == 5:
        return "fifth"
    elif num == 6:
        return "sixth"
    elif num == 7:
        return "seventh"
    elif num == 8:
        return "eighth"
    elif num == 9:
        return "ninth"
    elif num == 10:
        return "tenth"
    elif num == 11:
        return "eleventh"
    elif num == 12:
        return "twelfth"
    else:
        return ""
def main():
#Get the number whose ordinal no. you want to have.
    n=input("Enter a number: ")
#Check if the given no. is a digit or not.
    if not n.isdigit():
        print("Invalid")
    else:
#Call the get_ordinal function to print the ordinal no.
        print(get_ordinal(n))
if __name__ == "__main__":
    main()
