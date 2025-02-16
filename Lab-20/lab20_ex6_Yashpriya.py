import random
def insertion_sort(A):
        for j in range(1, len(A)):
            key=A[j]
            i=j-1
            while i>=0 and A[i] < key:
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key
        return A

def main():
    A = []
    for i in range(1, 50):
        a = random.randint(1, 50)
        A.append(a)
    print(f"Random array: {A}")
    print(f"Array sorted in descending order (insertion sort algorithm): {insertion_sort(A)}")
if __name__ == "__main__":
    main()

def selection_sort(B):
    def swap(i, j):
        temp = B[j]
        B[j] = B[i]
        B[i] = temp
    for i in range(len(B)-1):
        max_index=i
        for j in range(i+1, len(B)):
            if (B[j] > B[max_index]):
                max_index=j
        if max_index != i:
            swap(i, max_index)
    return B

def main():
    B=[]
    for i in range(1, 100):
        b = random.randint(1, 100)
        B.append(b)
    print(f"Random array: {B}")
    print(f"Array sorted in descending order (selection sort algorithm): {selection_sort(B)}")

if __name__ == "__main__":
    main()