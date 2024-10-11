def check_prime_or_composite(N):
    if N < 2:
        return False
    for i in range(2, int(N//2)+1):
           if N % i == 0:
               return False
    return True
def main():
    num=int(input('Enter a positive number: '))
    if check_prime_or_composite(num):
        print(num, 'is a prime number.')
    elif num == 0 or num == 1:
        print(num, 'is neither prime nor composite number.')
    else:
        print(num, 'is a composite number.')
if __name__ == "__main__":
    main()