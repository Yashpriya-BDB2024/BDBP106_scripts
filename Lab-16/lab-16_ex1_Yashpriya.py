# Get a non-negative decimal number from the user as input
num=int(input("Enter a non-negative number: "))
q=num
base=2
#Set the default empty string
result = ""
# Check if that number is non-negative
if q < 0:
    print('Please enter a non-negative number')
else:
        while q > 0:
            r = q%base
            result = str(r) + result
            q = q//2
#Print the binary representation
print("The binary representation is", result)
