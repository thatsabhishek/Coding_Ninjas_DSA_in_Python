# Write a program to determine if given number is palindrome or not. 
# Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
# Input : 121
# Output : true

def checkPalindrome(num):
	n = num
	sum = 0
	while(n != 0):
		r = n % 10
		sum = sum*10+r
		n = n//10
	return sum


num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome == num):
	print('true')
else:
	print('false')
