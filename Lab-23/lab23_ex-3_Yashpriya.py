# Part-a
def AddNumbers(x, y):
    return x+y
def SubtractNumbers(x, y):
    return x-y
def OperateNumbers(func, x, y):    # func - passed as a parameter/argument
    output=func(x, y)
    print(output)

def main():
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    sum_of_num = AddNumbers   # variable is storing the reference to the function - AddNumbers
    print(f"Sum: {sum_of_num(x, y)}")
    diff_of_num = SubtractNumbers
    print(f"Difference: {diff_of_num(x, y)}")
    OperateNumbers(sum_of_num, x, y)
    OperateNumbers(diff_of_num, x, y)
if __name__ == "__main__":
    main()

# Part-b
def ConcatenateStrings(str1, str2):
    return str1+str2
def ReplaceWord(str1, str2=""):
    return str1.replace(str1, str2)
def OperateStrings(func, str1, str2):
    output=func(str1, str2)
    print(output)

def main():
    str1=input("Enter the first string: ")
    str2=input("Enter the second string: ")
    concat_str=ConcatenateStrings
    replace_str=ReplaceWord
    OperateStrings(concat_str, str1, str2)
    OperateStrings(replace_str, str1, str2)
if __name__ == "__main__":
    main()