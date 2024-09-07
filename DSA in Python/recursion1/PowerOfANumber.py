# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
# Note : For this question, you can assume that 0 raised to the power of 0 is 1

# Sample Input 1 :
#  3 4
# Sample Output 1 :
# 81

def power(x,n):
    if n==1:
        return x
    elif n==0:
        return 1
    else:
        return x*power(x, n-1)

x, n = input().split()
x = int(x)
n = int(n)
print(power(x,n))