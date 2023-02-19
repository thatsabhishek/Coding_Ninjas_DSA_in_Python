# Write a Program to determine if the given number is Armstrong number or not. 
# Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that 
# the sum of its digits raised to nth power is equal to the number itself.
# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

num = int(input())
sum = 0
n = num
a = len(str(num))

while n != 0:
    r = n % 10
    sum = sum + r**a
    n = n // 10

if (sum == num):
    print('true')
else:
    print('false')
