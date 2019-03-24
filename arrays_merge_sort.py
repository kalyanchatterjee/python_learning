from array import array
import math

# Array typecodes
# https://docs.python.org/2/library/array.html

numbers = array('i', [1, 2, 34, 4, 6, 7, 2, 3, 5, 28, 9])
# numbers.append(12)
# numbers.remove(34)
# numbers[0] = 8
# numbers[1] = 0.1 - returns an error

print("Original array: ", numbers)


def merge_sort(A):
    if len(A) < 2:
        return A
    else:
        midpoint = math.ceil((len(A)/2))
        lefthalf = A[0:midpoint]
        print("left: ", lefthalf)
        righthalf = A[midpoint:]
        print("right: ", righthalf)
        print("Calling merge ...")
        return merge(merge_sort(lefthalf), merge_sort(righthalf))


def merge(L, R):
    print("L is ", L)
    print("R is ", R)
    output = array('i')
    m = 0
    n = 0

    while (m < len(L) and n < len(R)):
        if L[m] <= R[n]:
            output.append(L[m])
            m = m + 1
        else:
            output.append(R[n])
            n = n + 1

    # Check if either L or R have an element left
    if (m < len(L)):
        for i in range(m, len(L)):
            output.append(L[i])

    if (n < len(R)):
        for j in range(n, len(R)):
            output.append(R[j])

    return(output)


print(merge_sort(numbers))
