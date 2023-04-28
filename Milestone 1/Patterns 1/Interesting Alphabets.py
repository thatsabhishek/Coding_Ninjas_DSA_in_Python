# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

N = int(input())
i = 1
while i <= N:
    j = 1
    k = i
    while j <= i:
        ch = chr(ord('A')+N-k)
        print(ch, end='')
        k = k-1
        j = j+1
    print()
    i = i+1