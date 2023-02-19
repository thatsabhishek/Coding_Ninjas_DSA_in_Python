# Given an array of length N, you need to find and print the sum of all elements of the array.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces

n=int(input())
li=[int(x) for x in input().split()]
sum=0
for i in range(n):
    sum+=li[i]
print(sum)