# Print the following pattern for a given n.
# For eg. N = 6

# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

n = int(input())
i = 1
a = 1
while i <= n:
    sp = 1
    while sp < i:
        print(' ', end='')
        sp = sp+1
    for j in range(a, n+1):
        print(j, end='')
    print()
    a = a+1
    i = i+1
    j = j+1
i = 1
a = n-1
while i <= n-1:
    sp = 1
    while sp <= n-i-1:
        print(' ', end='')
        sp = sp+1
    for j in range(a, n+1):
        print(j, end='')
    print()
    i = i+1
    a = a-1
