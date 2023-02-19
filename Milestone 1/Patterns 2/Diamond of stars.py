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
s = (n+1)/2
while i <= s:
    sp = 1
    while sp <= s-i:
        print(' ', end='')
        sp = sp+1
    j = 1
    while j <= 2*i-1:
        print("*", end='')
        j = j+1
    print()
    i = i+1
i = s-1
m = i
while i >= 1:
    j = 1
    while j <= m-i+1:
        print(' ', end='')
        j = j+1
    k = 1
    while k <= 2*i-1:
        print("*", end='')
        k = k+1
    print()
    i = i-1
