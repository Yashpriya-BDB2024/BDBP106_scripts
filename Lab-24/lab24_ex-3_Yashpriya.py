# Part-a
g_counter=1
def counter_decorator(func):
    def wrapper():
        global g_counter
        g_counter+=1
        func()
        l_counter=10
        print(f"local counter: {l_counter}")
    return wrapper
@counter_decorator
def global_counter():
    print(f"global counter: {g_counter}")
n=int(input("How many times do you want to repeat? "))
for i in range(n):
    global_counter()

# Part-b
shared_value=5
def log_decorator(func):
    def wrapper(n):
        func(n)
        print(f"Current shared value: {shared_value}")
    return wrapper
@log_decorator
def add_to_shared_value(n):
    global shared_value
    shared_value+=n
@log_decorator
def multiply_shared_value(n):
    global shared_value
    shared_value*=n
n=int(input("Enter a number that you want to add or multiply to shared value: "))
add_to_shared_value(n)
multiply_shared_value(n)
add_to_shared_value(n)
multiply_shared_value(n)