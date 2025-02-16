def square(numbers):
    squares_list=[x**2 for x in numbers]
    squares_gen=(x**2 for x in numbers)
    print(f"Squares list: {squares_list}")
    print(f"Generator object: {squares_gen}")
    sq_list_itr=[]
    sq_gen_itr=[]
    for x in squares_list:
        sq_list_itr.append(x)
    print(f"Output after iterating over squares_list: {sq_list_itr}")
    for x in squares_gen:
        sq_gen_itr.append(x)
    print(f"Output after iterating over squares_gen: {sq_gen_itr}")

def even(numbers):
    even_list=[x for x in numbers if x%2==0]
    even_gen=(x for x in numbers if x%2==0)
    print(f"Even list: {even_list}")
    print(f"Generator object: {even_gen}")
    even_list_itr=[]
    even_gen_itr=[]
    for x in even_list:
        even_list_itr.append(x)
    print(f"Output after iterating over even_list: {even_list_itr}")
    for x in even_gen:
        even_gen_itr.append(x)
    print(f"Output after iterating over even_gen: {even_gen_itr}")

def main():
    numbers=[]
    for i in range(1, 11):
        numbers.append(i)
    print(f"Numbers: {numbers}")
    square(numbers)
    even(numbers)
if __name__ == "__main__":
    main()