# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1

N = int(input())
i = N
while i >= 1:
    j = 1
    while j <= i:
        print(j, end='')
        j = j+1
    print()
    i = i-1
