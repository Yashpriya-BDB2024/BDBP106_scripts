#get the first number as input
n1=int(input("Enter the first number: "))
#get the second number as input
n2=int(input("Enter the second number: "))
#get the operator as input
op=input("Enter the operator: ")
#Perform following operations using 'if' blocks and print the respective statements
if op == '+':
    sum=n1+n2
    print("The sum of first number", n1, "and second number", n2, "is", sum)
if op == '-':
    difference=n1-n2
    print("The difference of both the numbers", n1, "and", n2, "is", difference)
if op == '*':
    product=n1*n2
    print("The product of both the numbers", n1, "and", n2, "is", product)
if op == '/':
    quotient=n1/n2
    print("The quotient is", quotient)
if op == '%':
    remainder=n1%n2
    print("The remainder is", remainder)
if op == '**':
    exponent=n1**n2
    print("The power of", n1, "to", n2, "is", exponent) 

    
    


