"""QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.
"""

def partition(A, low, high):
    x = A[high]             # Picks the last element as the pivot
    i = low - 1
    for j in range(low, high):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]   #Swap Pivot at high with element at i+1
    return i+1


def quick_sort(A, low, high):
    if low < high:
        q = partition(A,low,high)
        quick_sort(A, low, q-1)
        quick_sort(A, q+1, high)
    return A


if __name__ == "__main__":
    A = [2,4,9,7,6,5]
    print(quick_sort(A, 0, len(A)-1))

