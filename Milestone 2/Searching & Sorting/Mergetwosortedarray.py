# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third array/list such that the third array is also sorted.

# Input Format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
# Second line contains 'N' single space separated integers representing the elements of the first array/list.
# Third line contains an integer 'M' representing the size of the second array/list.
# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

from sys import stdin

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    arr3 = []
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i+1
        else:
            arr3.append(arr2[j])
            j = j+1
    while i < n:
        arr3.append(arr1[i])
        i = i+1
    while j < m:
        arr3.append(arr2[j])
        j = j+1
    return arr3


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1