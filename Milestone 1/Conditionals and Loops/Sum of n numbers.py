# Given an integer n, find and print the sum of numbers from 1 to n.
# Note: Use while loop only.

n = int(input())
sum = 0
while(n != 0):
    sum = sum+n
    n = n-1
print(sum)
