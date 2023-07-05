# Given an integer array A of size n. Find and print all the leaders present in the input array. 
# An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
# Print all the leader elements separated by space and in the same order they are present in the input array.

# Sample Input 1 :
# 6
# 3 12 34 2 0 -1
# Sample Output 1 :
# 34 2 0 -1

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
arr = list(map(int, input().split()))
ma = arr[-1]
arr = arr[::-1]
k = [arr[0]]
for i in range(1, n):
    if arr[i] >= ma:
        ma = arr[i]
        k.append(arr[i])
k = k[::-1]
print(*k)