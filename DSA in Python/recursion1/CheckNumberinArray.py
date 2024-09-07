# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
# Do this recursively.
# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true

def checkNumber(arr, x):
    if len(arr) == 0:
        return False
    elif arr[0] == x:
        return True
    else:
        return checkNumber(arr[1:], x)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
