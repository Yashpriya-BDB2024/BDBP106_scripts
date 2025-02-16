#To determine the LCM of two numbers 'm' and 'n'
def lcm(m, n):
    if m > n:
        largest = m
    else:
        largest = n
    while largest > 0:
        if largest % m == 0 and largest % n == 0:
            return largest
        largest += 1
def main():
    m=int(input("Enter the first positive integer: "))
    n=int(input("Enter the second positive integer: "))
    result=lcm(m, n)
    print(f"The LCM of {m} and {n} is {result}")
if __name__ == "__main__":
    main()