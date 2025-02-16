import random
def create_exponent(n):
    return lambda x: x**n   # returns lambda function that raises x to the power of n
create_4th_exponent=create_exponent(4)
create_5th_exponent=create_exponent(5)
def main():
    N = 10
    list_1 = []
    for num in range(1, N + 1):
        rand_num = random.randint(1, 10)
        list_1.append(rand_num)
    print(f"List-1: {list_1}")

    result=[create_4th_exponent(x) for x in list_1]
    print(f"4th exponent: {result}")
    result=[create_5th_exponent(x) for x in list_1]
    print(f"5th exponent: {result}")
if __name__ == "__main__":
    main()