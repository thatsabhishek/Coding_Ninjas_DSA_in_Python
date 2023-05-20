# You are given an integer array/list(ARR) of size N. 
# It contains only 0s, 1s and 2s. Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.
# Note: You need to change in the given array/list itself. Hence, no need to return or print anything. 
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
# Second line contains 'N' single space separated integers(all 0s, 1s and 2s) representing the elements in the array/list.

from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    nextZero = 0
    nextTwo = (n - 1)
    i = 0
    while i <= nextTwo:
        if arr[i] == 0:
            arr[nextZero], arr[i] = arr[i], arr[nextZero]
            i += 1
            nextZero += 1

        elif arr[i] == 2:
            arr[nextTwo], arr[i] = arr[i], arr[nextTwo]
            nextTwo -= 1
    
        else:
            i += 1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1