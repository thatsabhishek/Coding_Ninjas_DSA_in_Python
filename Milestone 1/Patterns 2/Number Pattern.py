# Print the following pattern for n number of rows.
# Pattern for N=5
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j = j+1
    sp = 1
    while sp <= 2*(n-i):
        print(' ', end='')
        sp = sp+1
    k = i
    m = 1
    while m <= i:
        print(k, end='')
        k = k-1
        m = m+1
    print()
    i = i+1