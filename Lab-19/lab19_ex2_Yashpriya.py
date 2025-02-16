import random

List=[]
random_length=random.randint(100, 200)
for num in range(1, random_length+1):
    random_number=random.randint(100, 200)
    List.append(random_number)
print(List)

def first_and_second_half(List):
    first_half=List[:len(List)//2]
    print(f"First half of the list: {first_half}")
    second_half=List[len(List)//2:]
    print(f"Second half of the list: {second_half}")

#Print the elements whose occurrence is more than 1
    set_list=set(List)
    print(f"Elements occurring more than once: {set_list}")

#Print the elements whose occurrence is only once
    unique_elements_list=[]
    for num in List:
        if List.count(num)==1:
            unique_elements_list.append(num)
    print(f"Unique elements: {unique_elements_list}")

def main():
    first_and_second_half(List)
if __name__ == "__main__":
    main()
