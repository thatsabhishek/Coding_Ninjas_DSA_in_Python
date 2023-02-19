# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234

n = int(input())
i = 1
while i <= n:
    sp = 1
    while sp <= n-i:
        print(' ', end='')
        sp = sp+1
    j = i
    while j >= 1:
        print(j, end='')
        j = j-1
    k = 2
    while k <= i:
        print(k, end='')
        k = k+1
    print()
    i = i+1
