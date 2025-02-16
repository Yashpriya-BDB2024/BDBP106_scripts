# Use of generators - yield & next()
# Part-a
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a1=a
        a=b
        b=a1+a
fib_gen=fibonacci()
print("Fibonacci series: ")
for _ in range(1, 11):
    print(next(fib_gen))

# Part-b
def even_numbers():
    even=0
    while True:
        yield even
        even += 2
even_gen=even_numbers()
print("Even numbers: ")
for _ in range(1, 11):
    print(next(even_gen))

# Part-c
def powers_of_2():
    n=0
    while True:
        yield 2**n
        n+=1
power_gen=powers_of_2()
print("Powers of 2: ")
for _ in range(1, 11):
    print(next(power_gen))