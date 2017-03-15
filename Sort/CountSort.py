"""Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing).
Then doing some arithmetic to calculate the position of each object in the output sequence"""

# RUNTIME --> O(n+k); where, n --> no of elements
# and k --> range of input

# 1. Counting sort is efficient if the range of input is not significantly greater than the
# number of objects to be sorted i.e. k >> n
# Example: when the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
# 2. It is not comparison based sorting
# 3. It is often used as a subroutine to another sorting algorithm like radix sort.
# 4. Can be made to work for negative input as well.

def count_sort(A):

    # The ouput character array that will have sorted array
    output = [0 for i in range(len(A))]
    temp = []

    for i in A:
        if type(i) == int:
            temp.append(i)
        elif isinstance(i,str) :
            temp.append(ord(i))

    minimum, maximum = min(temp), max(temp)

    # Count array to store the count of individual element
    count = [0 for i in range(minimum-1, maximum+1)]

    # Store count of each character
    for i in temp:
        count[i] += 1 # ord --> gives the corresponding ASCII values the character string

    # Summing up the adjacent counts
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Building output array containing the sorted elements
    for i in range(len(temp)):
        output[count[temp[i]]-1] = temp[i]
        count[temp[i]] -= 1

    A = list(output)

    # Clearing unused lists
    del temp[:]
    del output[:]
    del count[:]

    return A

if __name__ == "__main__":
    print(count_sort(['a','b',4,2,1,100,50,'e',6,9,5,1]))