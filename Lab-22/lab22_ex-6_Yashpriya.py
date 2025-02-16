import random

def merge_sort(A, p, r):  # p: index of the first element & r: index of the last element
    if p < r:
        q=(p + r)//2     # q: middle index
        merge_sort(A, p, q)    # to sort the left sub-array from p to q
        merge_sort(A, q+1, r)    # to sort the right sub-array from index q+1 to r
        merge(A, p, q, r)     # to combine above sorted sub-arrays back to a single sorted array.

def merge(A, p, q, r):
    n1=q-p+1   # no. of elements in the left subarray
    n2=r-q     # no. of elements in the right subarray
    left_subarray = []
    right_subarray = []
    for i in range(n1):
        left_subarray.append(A[p + i])    # Append elements from index p to q to left subarray
    for j in range(n2):
        right_subarray.append(A[q + 1 + j])   # Append elements from index q+1 to r to right subarray
    k = l = 0  # k - left subarray index,  l - right subarray index - initialized to 0
    for x in range(p, r + 1):
        if k < n1 and (l >= n2 or left_subarray[k] <= right_subarray[l]):   # If the element in left subarray is less than the element in right subarray
            A[x] = left_subarray[k]  # Take the current element from left subarray
            k += 1   # Move to the next element in the left subarray
        else:
            A[x] = right_subarray[l]
            l += 1

def main():
    A = []
    for i in range(1, 11):
        rand_num = random.randint(1, 10)
        A.append(rand_num)
    print(f"Random array: {A}")
    N = len(A)
    merge_sort(A, 0, N - 1)
    print(f"Sorted array: {A}")

if __name__ == "__main__":
    main()