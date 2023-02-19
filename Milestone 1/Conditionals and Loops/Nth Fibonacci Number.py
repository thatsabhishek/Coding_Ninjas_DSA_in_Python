# Nth term of Fibonacci series F(n), where F(n) is a function, 
# is calculated using the following formula -
#     F(n) = F(n-1) + F(n-2), 
#     Where, F(1) =  1, 
#            F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number.

def fact(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        sum = 0
        a = 1
        b = 1
        while n-1 != 0:
            sum += a
            a = b
            b = sum
            n=n-1
        return sum
    
n = int(input())
print(fact(n))
