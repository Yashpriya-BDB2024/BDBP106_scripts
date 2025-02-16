# Variation in exercise-6
def calculator(func):
    def wrapper(*args):
        print("Basic arithmetic operation.")
        print(func(*args))
        print("Operation completed successfully.")
    return wrapper
@calculator
def arithmetic_ops(a, b, key):
    arith_dict = {"sum": a+b, "difference": a-b, "product": a*b, "quotient": a/b if b!=0 else "Error", "remainder": a%b if b!=0 else "Error"}
    return arith_dict[key]
def main():
    while True:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        key=input("Enter the operation name: ")
        if key=='q':
            break
        arithmetic_ops(a, b, key)
if __name__ == "__main__":
    main()