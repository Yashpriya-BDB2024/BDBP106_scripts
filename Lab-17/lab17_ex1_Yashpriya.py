from random import randint
#Set the values of global variables
SHORTEST=7
LONGEST=10
MIN_ASCII=33
MAX_ASCII=126
def randomPassword():
#It will pick the length of the password randomly between 7 and 10
    randomLength=randint(SHORTEST, LONGEST)
#Set the default empty string
    result=""
#This 'for' loop will append the character from the above given ASCII range to the result
    for i in range(randomLength):
        randomChar=chr(randint(MIN_ASCII, MAX_ASCII))
        result += randomChar
    return result
def main():
#It will print the final password via calling the randomPassword() function
    print("Your random password is", randomPassword())
if __name__ == "__main__":
#Calling the main function
    main()
