# Problem statement
# For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
# Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is equal to the sum of elements at indices [(i + 1) to (N-1)]. 
# One thing to note here is, the item at the index 'i' is not included in either part.
# If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned. Negative one(-1) if no such index is present.

from sys import stdin

def arrayEquilibriumIndex(arr,n):
    n=len(arr)
    leftsum=0
    rightsum=0
    for i in range(n):
        rightsum+=arr[i]
    for i in range(n):
      rightsum-=arr[i]
      if leftsum==rightsum:
            return i
      leftsum+=arr[i]
    return -1 




#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1