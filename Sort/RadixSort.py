"""For elements in the range 1 to n^2, we can't use Counting SOrt as it will take O(n^2)
which is worse than comparion based sorting algorithms
RADIX SORT does digit by digit sort starting from least significant digit to most significant digit.
It uses Counting Sort as a subroutine to sort.
We sort the numbers from Least siginificant digit to the most significatn digit.
It is only used to sort numbers"""

# TIME COMPLEXITY : O(kn) , where k is the legth of the longest number and n is the size of the input array
# We can also make the radix to make k less than log(n)

def count_sort(A, exp):
    n = len(A)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (A[i] // exp)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (A[i] / exp)
        output[count[int((index) % 10)] - 1] = A[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]



def radix_sort(A):

    # Finds the maximum number to know the number of digits
    max_elmnt = max(A)

    exp = 1
    while max_elmnt/exp > 0:
        count_sort(A, exp)
        exp *= 10
    return A

if __name__ == "__main__":
    A = [9,179,139,38,10,5,36]
    print(radix_sort(A))

