# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG

N = int(input())
i = 1
while i <= N:
    j = 1
    k = i
    while j <= i:
        print(chr(65+k-1), end='')
        k = k+1
        j = j+1
    print()
    i = i+1
