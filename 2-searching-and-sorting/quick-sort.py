"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    low, high = 0, len(array)-1
    qsort(array, low, high)
    return array

def qsort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        qsort(array, low, pi-1)

        # Recursive call on the right of pivot
        qsort(array, pi+1, high)


def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))