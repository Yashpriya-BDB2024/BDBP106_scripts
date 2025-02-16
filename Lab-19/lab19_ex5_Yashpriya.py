import random

def list_comprehension_usage():
#To make a list of 100 random numbers
    num_list=[]
    length=100
    for num in range(1, length+1):
        rand_num=random.randint(1, 100)
        num_list.append(rand_num)
    print(f"The list containing randomly generated numbers: {num_list}")

#To print the square of each even no.
#It will check each no. in the random no. list, if its even, then only it will compute the square of each one.
    square_list=[(i*i) for i in num_list if i%2==0]
    print(f"The list containing square of each even no.: {square_list}")

#To print the cube of each odd no.
#It will check each no. in the random no. list, if its odd, then only it will compute the cube of each one.
    cube_list=[(i*i*i) for i in num_list if i%2==1]
    print(f"The list containing cube of each odd no.: {cube_list}")

def main():
    list_comprehension_usage()
if __name__ == "__main__":
    main()
