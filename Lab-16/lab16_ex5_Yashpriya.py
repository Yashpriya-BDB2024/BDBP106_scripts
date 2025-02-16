#Get 8 bits at a time as input
line=input("Enter 8 bits: ")
if line.count("0")+line.count("1")!=8 or len(line)!=8:
    print("Please enter 8 bits at a time")
else:
    ones=line.count("1")
    if ones%2==0:
        print("Parity bit is 0")
    else:
        print("Parity bit is 1")