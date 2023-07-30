# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.
# Sample Input 1 :
# 3
# 9 8 9
# Sample Output 1 :
# 26

def sumArray(arr):
    n = len(arr)
    if n==0:
        return 0
    else:
        return arr[0] + sumArray(arr[1:])

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
