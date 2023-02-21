# You are given two numbers, ‘X’ and ‘Y’. 
# Your task is to find the greatest common divisor of the given two numbers.
# The Greatest Common Divisor of any two integers is the largest number that divides both integers.

# Input :
# 2
# 20 15
# 8 32
# Output :
# 5
# 8

def findGcd(x, y):
    while y:
        x, y = y, x % y
    return x

# this part of the code not used in the coding ninja compiler.
t=int(input())
while t!=0:
    x,y=input().split()
    x,y=int(x),int(y)
    print(findGcd(x,y))
    t=t-1
