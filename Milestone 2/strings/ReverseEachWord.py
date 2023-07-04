# Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed. A word is a combination of characters without any spaces.
# Example:
# Input Sentence: "Hello, I am Aadil!"
# The expected output will print, ",olleH I ma !lidaA".


from sys import stdin


def reverseEachWord(string) :
	s = string
	new = s.split()
	ns = ''
	for i in range(len(new)):
		sad = new[i][::-1]
		ns = ns+sad+' '
	return ns


#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)