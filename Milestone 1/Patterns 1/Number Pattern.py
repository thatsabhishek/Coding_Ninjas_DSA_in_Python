# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1

N = int(input())
i = 1
while i <= N:
    j = 1
    while j <= N-i+1:
        print(j, end='')
        j = j+1
    print()
    i = i+1
