# Ninja was playing with her sister to solve a puzzle pattern. However, 
# even after taking several hours, they could not solve the problem.
# A value of N is given to them, and they are asked to solve the problem. 
# Since they are stuck for a while, they ask you to solve the problem. 
# Can you help solve this problem?

# Input :
# 2
# 3
# 2
# Output :
# ***
#  **     
#   *

# **
#  *    


def ninjaPuzzle(n):
    i=1
    while i<=n:
        sp=1
        while sp<i:
            print(' ',end='')
            sp=sp+1
        j=1
        while j<=n-i+1:
            print('*',end='')
            j=j+1
        print()
        i=i+1
    return 0

# this part of the code not used in the coding ninja compiler.
t=int(input())
while t !=0 :
    n = int(input())
    ninjaPuzzle(n)
    t=t-1
