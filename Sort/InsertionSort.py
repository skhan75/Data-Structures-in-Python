def insertions_sort(A):
    for i in range(1, len(A)):          # from 1 to n-1
        key = A[i]
        j = i
        while j > 0 and A[j-1] > key:
            A[j] = A[j-1]
            j -= 1
        A[j] = key
    return A


if __name__ == "__main__":
   print (insertions_sort([2,3,1,4,6,9,7]))