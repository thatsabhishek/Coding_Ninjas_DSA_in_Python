# Print the following pattern for the given number of rows.
# Note: N is always odd.
# Pattern for N = 5
#    *
#   ***
#  *****
#   ***
#    *

n = int(input())
u = n//2+1
i=1
while i<=u:
    sp = 1
    while sp<=u-i:
        print(' ', end='')
        sp+=1
    j = 1
    while j <= 2*i-1:
        print("*", end='')
        j+=1
    print()
    i+=1

l = n-u
i=1
while i <= n-u:
    sp = 1
    while sp <= i:
        print(' ', end='')
        sp+=1
    j = 1
    while j <= 2*l-1:
        print("*", end='')
        j+=1
    print()
    i+=1
    l-=1 