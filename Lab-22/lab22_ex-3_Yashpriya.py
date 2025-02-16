import random
def apply_operation(a, b, operation):
    return operation(a, b)
sum=lambda a, b: a+b
quotient=lambda a, b: "%5.2f" % (a/b)
product=lambda a, b: a*b
difference=lambda a, b: a-b

def main():
    N=10
    list_1=[]
    for num in range(1, N+1):
        rand_num=random.randint(1, 10)
        list_1.append(rand_num)
    print(f"List-1: {list_1}")
    N=10
    list_2 = []
    for y in range(1, N+1):
        rand_num = random.randint(1, 10)
        list_2.append(rand_num)
    print(f"List-2: {list_2}")

    result=[apply_operation(a, b, sum) for a, b in zip(list_1, list_2)]
    print(f"Sum: {result}")
    result=[apply_operation(a, b, quotient) for a, b in zip(list_1, list_2)]
    print(f"Quotient: {result}")
    result=[apply_operation(a, b, product) for a, b in zip(list_1, list_2)]
    print(f"Product: {result}")
    result=[apply_operation(a, b, difference) for a, b in zip(list_1, list_2)]
    print(f"Difference: {result}")

if __name__ == "__main__":
    main()