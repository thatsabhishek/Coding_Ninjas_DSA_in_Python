# Print the following pattern for the given number of rows.
# Note: N is always odd.
# Pattern for N = 5
#   *
#  ***
# *****
#  ***
#   *

n = int(input())
i = 1
s1 = (n+1)/2
while i <= s1:
    sp = 1
    while sp <= s1-i:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= 2*i-1:
        print('*', end='')
        j = j+1
    print()
    i = i+1

i = 1
s2 = n-s1
while i <= s2:
    sp = 1
    while sp <= i:
        print(' ', end='')
        sp += 1
    k = 1
    while k <= n-2*i:
        print("*", end='')
        k = k+1
    print()
    i = i+1