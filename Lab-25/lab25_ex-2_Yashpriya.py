def calculator(n1, n2, op):
    try:
        if op=='+':
            return n1+n2
        elif op=='-':
            return n1-n2
        elif op=='*':
            return n1*n2
        elif op == '/':
            return n1/n2
        else:
            raise ValueError
    except ValueError:
        print("Value error: Invalid operator")
    except ZeroDivisionError:
        print("Zero Division error: Denominator can't be zero")
    finally:
        print("Arithmetic operation done successfully.")
def main():
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    op=input("Enter an arithmetic operator: ")
    print(calculator(n1, n2, op))
if __name__ == "__main__":
    main()
