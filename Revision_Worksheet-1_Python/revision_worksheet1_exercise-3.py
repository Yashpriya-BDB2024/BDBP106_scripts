def calculate_median(n1, n2, n3):
    numbers=[n1, n2, n3]
    numbers.sort()   #To calculate median, firstly the data set needs to be sorted.
    n=len(numbers)
    term=(n+1)//2
    median=numbers[term-1]
    return median
def main():
    n1=int(input("Enter the first number: "))
    n2= int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    result=calculate_median(n1, n2, n3)
    print(f"The median of {n1}, {n2} and {n3} is {result}")
if __name__ == "__main__":
    main()