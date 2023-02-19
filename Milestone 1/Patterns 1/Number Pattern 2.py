# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003

N = int(input())
i = 2
print(1)
while i <= N:
    j = 1
    while j <= i:
        if (j == 1 or j == i):
            print(i-1, end='')
        else:
            print(0, end='')
        j = j+1
    print()
    i = i+1
