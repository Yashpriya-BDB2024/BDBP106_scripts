def isInteger(s):
#Removes the white spaces
    s=s.strip()
#Checks if the string is positive or negative
    if(s[0]=='+' or s[0]=='-') and s[1:].isdigit():
        return True
    elif s.isdigit():
        return True
    else:
        return False
def main():
#Get the integer string as input
    str=input("Enter the string: ")
    if isInteger(str):
        print("The string", str, "is an integer")
    else:
        print("The string", str, "is not an integer")
if __name__ == "__main__":
    main()
