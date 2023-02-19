# Given a number N, print sum of all even numbers from 1 to N.

N = int(input())
sum = 0
if(N % 2 == 0):
    while(N != 0):
        sum = sum+N
        N = N-2
else:
    N = N-1
    while(N != 0):
        sum = sum+N
        N = N-2
print(sum)
