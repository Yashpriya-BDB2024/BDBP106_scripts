# Use of decorators - wrapper & @func
# Part-a
dic1={"Jane Austen": ["Pride and Prejudice", "Sense and Sensibility"], "Charles Dickens": ["Oliver Twist", "Pickwick Papers"]}
def addPreface(func):
    def wrapper(*args):
        print("These are the authors of Classical English Literature: ")
        func(*args)
        print("They are to be enjoyed.")
    return wrapper
@addPreface
def ListBooksByAuthor(auth):
    for author in auth:
        author=author.strip()  # To trim any white-spaces
        print(author)
        print(f"Books: {dic1[author]}")
def main():
    auth=input("Enter author(s) (separated by comma): ").split(',')
    ListBooksByAuthor(auth)
if __name__ == '__main__':
    main()

# Part-b
import time
def log_execute(func):
    def wrapper(*args, **kwargs):
        begin=time.time()
        print(f"Entering function {func.__name__} at {begin}")
        print(f"Sum: {func(*args, **kwargs)}")
        end=time.time()
        print(f"Exiting function {func.__name__} at {end}")
    return wrapper
@log_execute
def addTwoNumbers(a, b):
    return a+b
def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    addTwoNumbers(a,b)
if __name__ == '__main__':
    main()







