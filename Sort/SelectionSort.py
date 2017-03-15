"""ALGORTIHM:
       The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
       The algorithm maintains two subarrays in a given array.

        1) The subarray which is already sorted.
        2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.  """

def selection_sort(A):
    n = len(A)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if A[min_idx] > A[j]:
                min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

    return A

if __name__ == "__main__":
    print (selection_sort([4,3,5,8,2]))

