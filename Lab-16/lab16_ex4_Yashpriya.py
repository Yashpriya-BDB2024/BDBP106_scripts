# Get the palindrome string as input
line = input("Enter the palindrome string: ")
#Convert the string into lower case
line=line.lower()
# Check if the string is a palindrome
for i in range(len(line) // 2):
    if line[i] != line[len(line) - i - 1]:
        print('The given string is not a palindrome')
        break
else:
    print('The given string is a palindrome')