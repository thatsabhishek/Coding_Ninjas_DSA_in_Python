# Given the 'start' and the 'end'' positions of the array 'input'. 
# Your task is to sort the elements between 'start' and 'end' using quick sort.

# Note :
#     Make changes in the input array itself.

from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex < endIndex:
        # Partition the array
        pivotIndex = partition(arr, startIndex, endIndex)

        # Recursively sort the left and right subarrays
        quickSort(arr, startIndex, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, endIndex)

def partition(arr: List[int], startIndex: int, endIndex: int) -> int:
    # Choose the pivot element (in this implementation, we choose the last element as the pivot)
    pivot = arr[endIndex]

    # Index of the smaller element
    i = startIndex - 1

    for j in range(startIndex, endIndex):
        # If the current element is smaller than the pivot
        if arr[j] < pivot:
            # Increment the index of the smaller element
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at index i+1
    arr[i + 1], arr[endIndex] = arr[endIndex], arr[i + 1]

    return i + 1