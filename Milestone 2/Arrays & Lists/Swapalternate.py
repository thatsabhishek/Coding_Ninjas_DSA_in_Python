# You have been given an array/list(ARR) of size N. 
# You need to swap every pair of alternate elements in the array/list.
# You don't need to print or return anything, just change in the input array itself.

from sys import stdin

def swapAlternate(arr, n) :
    l = len(arr)
    i = 0
    while i < l-1:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2 
    return arr


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1