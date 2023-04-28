# Print the following pattern for the given N number of rows.
# Pattern for N = 5
#  A
#  BB
#  CCC
#  DDDD
#  EEEEE

N = int(input())
i = 1
while i <= N:
    j = 1
    while j <= i:
        ch = chr(ord('A')+i-1)
        print(ch, end='')
        j = j+1
    print()
    i = i+1
