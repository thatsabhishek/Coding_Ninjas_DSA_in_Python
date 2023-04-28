# Print the following pattern
# Pattern for N = 4
#    *
#   ***
#  *****
# *******

n = int(input())
i = 1
while i <= n:
    sp = 1
    while sp <= n-i:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= 2*i-1:
        print('*', end='')
        j = j+1
    print()
    i = i+1
