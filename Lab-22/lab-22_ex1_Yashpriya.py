import random
def product_func(list_1, list_2):
    product=lambda x, y: x*y
    result=[product(x, y) for x, y in zip(list_1, list_2)]   # zip() - unpacking - will take x & y from list-1 & list-2 respectively to compute the product of each pair.
    print(f"Product of each element of list_1 & list_2: {result}")

def square_func(list_1):
    square=lambda x: x*x
    result=[square(x) for x in list_1]  # to compute square of each element in list-1
    print(f"Square of each element in list_1: {result}")
    return result

def cube_func(list_1):
    cube=lambda x: x*x*x
    result=[cube(x) for x in list_1]  # to compute cube of each element in list-1
    print(f"Cube of each element in list_1: {result}")
    return result

def even_func(list_1):
# 'even' is a list of booleans
    even=lambda x:True if x%2==0 else False # if the remainder comes 0, then it will print true, otherwise false (for each element in list-1)
    result=[even(x) for x in list_1]
    print(f"Boolean list for checking even no. in list_1: {result}")

# To filter out only the even elements from the list_1
    filter_even=list(filter(even, list_1))
    print(f"Even numbers present in list_1: {filter_even}")

def odd_func(list_1):
# 'odd' is a list of booleans
    odd=lambda x:True if x%2==1 else False  # if the remainder comes 1, then it will print true, otherwise false (for each element in list-1)
    result=[odd(x) for x in list_1]
    print(f"Boolean list for checking odd no. in list_1: {result}")

# To filter out only the odd elements from the list_1
    filter_odd=list(filter(odd, list_1))
    print(f"Odd numbers present in list_1: {filter_odd}")

def square_cube_func(list_1):
    result=square_func(cube_func(list_1))  # cube function is given as a parameter to the square function
    print(f"Square of the cube of each element in list_1: {result}")

def main():
    N=100
    list_1=[]
    for num in range(1, N+1):
        rand_num=random.randint(0, 100)
        list_1.append(rand_num)
    print(f"List-1: {list_1}")
    N=100
    list_2 = []
    for y in range(1, N+1):
        rand_num = random.randint(0, 100)
        list_2.append(rand_num)
    print(f"List-2: {list_2}")

    product_func(list_1, list_2)
    square_func(list_1)
    cube_func(list_1)
    even_func(list_1)
    odd_func(list_1)
    square_cube_func(list_1)

if __name__ == "__main__":
    main()
