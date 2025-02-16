# To determine the greatest common divisor of integers 'm' and 'n'.
def greatest_common_divisor(m, n):
    if m < n:
        smallest = m
    else:
        smallest = n
    while smallest > 0:
        if m % smallest == 0 and n % smallest == 0:
            return smallest
        smallest -= 1
def main():
    m = int(input("Enter the first positive integer: "))
    n = int(input("Enter the second positive integer: "))
    result = greatest_common_divisor(m, n)
    print("The gcd of", m, "and", n, "is", result)
if __name__ == "__main__":
    main()
