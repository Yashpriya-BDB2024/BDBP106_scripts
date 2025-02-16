import random
def bubble_sort(A):
#To sort in ascending order -
#Vanilla algorithm
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp
    return A

#Improvised bubble sort
def improvised_bubble_sort(A):
    for i in range(len(A)-1):
        swap=False
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp
                swap=True
        if swap==False:
           break
    return A

#To sort in descending order
def descending_bubble_sort(A):
    for i in range(len(A)-1):
        swap=False
        for j in range(len(A)-1, i, -1):
            if A[j] > A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp
                swap=True
        if swap==False:
           break
    return A

def main():
    A=[]
    for i in range(1,100):
        a=random.randint(1, 100)
        A.append(a)
    print(A)
    print(f"Sorted array (with vanilla algorithm): {bubble_sort(A)}")
    print(f"Sorted array (with improvised algorithm): {improvised_bubble_sort(A)}")
    print(f"Sorted array (in descending order; improvised algorithm): {descending_bubble_sort(A)}")

if __name__ == "__main__":
    main()
