def get_square(num):
    if num==0:
        return None
    else:
        square=num*num
        return square
def get_cube(num):
    if num==0:
        return None
    else:
        cube=num*num*num
        return cube
def main():
    num=(int(input("Enter a number: ")))
    sq=get_square(num)
    print(f"The square of {num} is {sq}")
    cube=get_cube(num)
    print(f"The cube of {num} is {cube}")
if __name__ == "__main__":
    main()
