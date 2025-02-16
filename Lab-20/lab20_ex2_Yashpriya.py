def zip_usage(X, Y, Z):
    for name, dish, restaurant in zip(X, Y, Z):
        print(name, 'likes to eat', dish, 'at', restaurant)

def transpose_of_matrix():
    matrix=[[1,2,3], [3,4,5], [5,6,7]]
    transpose_matrix=[]
    for row in zip(*matrix):
        transpose_matrix.append(list(row))
    print(f"Transpose matrix (without comprehension): {transpose_matrix}")

    transpose=[i for i in zip(*matrix)]
    print(f"Transpose matrix (with comprehension): {transpose}")

def main():
    X=[]
    Y=[]
    Z=[]
    for i in range(1, 2):
        friend_name=input("Enter your friend name: ")
        fav_dish=input("Enter the favourite dish of your friend: ")
        fav_restaurant=input("Enter your friend's favourite restaurant: ")
        X.append(friend_name)
        Y.append(fav_dish)
        Z.append(fav_restaurant)
    print(X)
    print(Y)
    print(Z)
    zip_usage(X, Y, Z)
    transpose_of_matrix()

if __name__ =="__main__":
    main()
