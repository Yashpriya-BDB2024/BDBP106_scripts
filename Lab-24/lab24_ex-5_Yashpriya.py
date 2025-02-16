# Part-a
def age(n):
    if n<0:
        print("Age cannot be negative.")
        return
    age_after_10_years=n+10
    print(f"Age after 10 years: {age_after_10_years }")
def main():
    try:
        n=int(input("Enter your age (in years): "))
        age(n)
    except ValueError:
        print("Something else broke.")
if __name__ == "__main__":
    main()

# Part-b
def division(num):
    if num<=0:
        print("No. must be greater than 0")
        return
    print(100//num)
def main():
    try:
        num=int(input("Enter a denominator: "))
        division(num)
    except ValueError:
        print(f"Something else broke.")
if __name__ == "__main__":
    main()
