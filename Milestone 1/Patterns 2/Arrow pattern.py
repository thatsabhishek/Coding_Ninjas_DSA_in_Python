# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

n = int(input())
i = 1
c = int(n/2) + 1
while i <= c:
    sp = 1
    while sp < 2*i-2:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= i:
        print('* ', end='')
        j = j+1
    print()
    i = i+1
i = 1
d = n-c
while i <= n-c:
    sp = 1
    while sp < d:
        if sp%2==0:
            continue
        else:
            print(' ', end='')
        sp = sp+1
    j = 1
    while j <= d:
        print('* ', end='')
        j = j+1
    print()
    i = i+1
    d = d-1
