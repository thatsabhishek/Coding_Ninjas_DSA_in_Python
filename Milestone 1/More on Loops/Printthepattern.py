# Print the following pattern for the given number of rows.
# Pattern for N = 5
#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10

n = int(input())
start = 1

for i in range(1,n+1):
    for j in range(start, start+n):
        print(j, end=' ')
    print()
    if i==((n+1)//2):
        if n%2 != 0:
            start = n*(n-2)+1
        else:
            start = n*(n-1)+1
    elif i>(n+1)//2:
        start = start - 2*n
    else:
        start = start + 2*n