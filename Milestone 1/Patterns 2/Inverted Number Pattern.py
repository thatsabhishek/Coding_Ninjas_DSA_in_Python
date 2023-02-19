# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 333
# 22
# 1

N = int(input())
i = 1
k = N
while i <= N:
    j = 1
    while j <= N-i+1:
        print(k, end='')
        j = j+1
    print()
    k = k-1
    i = i+1
