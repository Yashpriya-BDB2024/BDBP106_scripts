# Part-a
def upper_case_greet(func):
    def wrapper(message):
        upper_case=message.upper()
        func(upper_case)
    return wrapper
# Part-b
def repeat(n_times):
    def inner_decorator(func1):
        def wrapper(message):
            for i in range(n_times):
                func1(message)
        return wrapper
    return inner_decorator
@upper_case_greet
@repeat(int(input("How many times you want to repeat the message? ")))
def greet(message):
    print(message)
def main():
    message=input("Enter a message: ")
    greet(message)
if __name__ == "__main__":
    main()