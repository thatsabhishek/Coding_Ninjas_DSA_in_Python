# Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

# The string is compressed only when the repeated character count is more than 1.
# Note:
# Consecutive count of every character in the input string is less than or equal to 9. You are not required to print anything. It has already been taken care of. Just implement the given function and return the compressed string.

# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(input) :
	# Write your code here.
	a = input
	i = 0
	x = ''
	while(i < len(a)):
		j = i+1
		c = 1
		while j < len(a) and (a[i] == a[j]):
			j += 1
			c += 1
		if c == 1:
			x += a[i]
		else:
			x += a[i]+str(c)
		i = j
	return x



# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)