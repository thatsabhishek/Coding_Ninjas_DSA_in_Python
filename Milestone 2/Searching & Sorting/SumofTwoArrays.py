# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. 
# Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). 
# The idea here is to represent each array/list as an integer in itself of digits N and M.
# You need to find the sum of both the input arrays/list treating them as two integers and put the result in another array/list 
# i.e. output array/list will also contain only single digit at every index.

# Note:
# The sizes N and M can be different. 
# Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the size of the bigger array/list. Place 0 at the 0th index if there is no carry. 
# No need to print the elements of the output array/list.
# Using the function "sumOfTwoArrays", write the solution to the problem and store the answer inside this output array/list. 
# The main code will handle the printing of the output on its own.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
# Second line contains 'N' single space separated integers representing the elements of the first array/list.
# Third line contains an integer 'M' representing the size of the second array/list.
# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here
    i = n-1
    j = m-1
    carry = 0
    l = max(n, m)+1
    while i >= 0 and j >= 0:
        num = arr1[i]+arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
        j = j-1
    while i >= 0:
        num = arr1[i]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
    while j >= 0:
        num = arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        j = j-1
    if carry != 0:
        output[0] = carry




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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1