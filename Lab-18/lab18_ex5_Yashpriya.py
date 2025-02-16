#Firstly check whether a given number is prime or not.
def check_prime(N):
    N=int(N)
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1):
           if N % i == 0:
               return False
    return True
#To find the first prime number, i.e., larger than the given integer.
def nextPrime(n):
    next_num = n + 1
    while not check_prime(next_num):
        next_num += 1
    return next_num
def main():
    n=int(input("Enter a positive number: "))
    result=nextPrime(n)
    print(f"The first prime number, i.e., larger than {n} is {result}.")
if __name__ == "__main__":
    main()
