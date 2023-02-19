# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 1111
# 000
# 11
# 0

n = int(input())
m = n
for i in range(n):
    if i % 2 == 0:
        print(m*'1', end='')
    else:
        print(m*'0', end='')
    m -= 1
    print()
