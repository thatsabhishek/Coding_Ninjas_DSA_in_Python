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
inc = int(n/2) + 1
while i <= inc:
    sp = 1
    while sp < i:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= i:
        print('* ', end='')
        j = j+1 
    print()
    i = i+1
i = 1
dec = n-inc
while i <= n-inc:
    sp = 1
    while sp < dec:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= dec:
        print('* ', end='')
        j = j+1
    print()
    i = i+1
    dec = dec-1