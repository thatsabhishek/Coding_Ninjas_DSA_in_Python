# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   232
#  34543
# 4567654

n = int(input())
i = 1
while i <= n:
    sp = 1
    while sp <= n-i:
        print(' ', end='')
        sp = sp+1
    j = 1
    k = i
    while j <= i:
        print(k, end='')
        j = j+1
        k = k+1
    m = 2*i-2
    while m > i-1:
        print(m, end='')
        m = m-1
    print()
    i = i+1
