# Given a number N, figure out if it is a member of fibonacci series or not. 
# Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
#     F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1

# Input 1 : 5
# Output 1 : true
# Input 2 : 14
# Output 2 : false    


def checkMember(n):
    sum = 0
    a = 0
    b = 1
    N = n
    while n!=0:
        sum = a+b
        a = b
        b = sum
        n=n-1
        if sum == N:
            return True
        else:
            continue
    if sum == N:
        return True
    else:
        return False


n = int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
