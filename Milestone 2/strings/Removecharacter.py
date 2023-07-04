# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

# Note:
# You are not required to print anything explicitly. It has already been taken care of.

# Sample Input 1:
# aabccbaa
# a
# Sample Output 1:
# bccb


from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	s = string
	x=""
	for i in s:
		if i != ch:
			x=x+i
	return x



#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)