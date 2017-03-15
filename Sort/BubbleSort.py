def bubble_sort(A):
    for i in range(len(A)):

        # Last i elements are already in place
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] =  A[j+1], A[j]
    return A

if __name__ == "__main__":
    print (bubble_sort([5,2,4,9,6,8]))