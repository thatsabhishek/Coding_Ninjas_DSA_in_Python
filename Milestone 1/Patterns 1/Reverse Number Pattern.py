# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321

N = int(input())
i = 1
while i <= N:
    j = 1
    while j <= i:
        print(i-j+1, end='')
        j = j+1
    print()
    i = i+1
