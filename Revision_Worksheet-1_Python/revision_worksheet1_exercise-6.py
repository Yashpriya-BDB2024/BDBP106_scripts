def arithmetic_operations(a, b):
    if a==0 and b==0:
        return None
    else:
        sum=a+b
        difference=a-b
        product=a*b
        quotient=a/b
        quotient="%5.2f" % quotient
        remainder=a%b
        return sum, difference, product, quotient, remainder
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    result=arithmetic_operations(a, b)
    print(f"The sum, difference, product, quotient, and remainder of {a} and {b} are {result}.")
if __name__ == "__main__":
    main()
