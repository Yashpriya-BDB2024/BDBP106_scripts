def compute_square(num):
    square=num*num
    return square
def compute_cube(num):
    cube=num*num*num
    return cube

def nested_dict(N):
    dict={}
    for i in range(1, N+1):
        dict[i]={"square": compute_square(i), "cube": compute_cube(i)}
    print(f"Nested dictionary: {dict}")

def tuple_of_tuples(N):
    tup_of_tup=tuple((i, compute_square(i), compute_cube(i)) for i in range(1, N+1))
    print(f"Tuple of tuples: {tup_of_tup}")

def identity_matrix():
    identity_mat=[]
    for i in range(1, 11):
        row=[]
        for j in range(1, 11):
            if i==j:
                result=1
            else:
                result=0
            row.append(result)
        identity_mat.append(row)
    return identity_mat

def zip_usage():
    english_verbs=["run", "eat", "sleep", "write", "speak"]
    spanish_verbs=["correr", "comer", "dormir", "escribir", "hablar"]
    eng_spanish_dict=dict(zip(english_verbs, spanish_verbs))
    print(f"English-Spanish dictionary: {eng_spanish_dict}")

def main():
    N=int(input("Till what no. you want to compute square & cube? "))
    nested_dict(N)
    tuple_of_tuples(N)
    result=identity_matrix()
    print(f"Identity matrix: {result}")
    zip_usage()

if __name__ == "__main__":
    main()
